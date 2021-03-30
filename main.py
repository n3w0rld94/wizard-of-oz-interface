import atexit
import json
import random
import subprocess
from threading import Timer

import eventlet
from flask import Flask, Response, request, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from werkzeug.routing import BaseConverter
from flask_mongoengine import MongoEngine

from models.user_status import Animus_User
from woz_utils.server_user import Server_User
from woz_utils.server_utils import (get_failure_response,
                                    get_failure_response_body,
                                    get_missing_user_response,
                                    get_success_response,
                                    get_success_response_body, open_browser)
from woz_utils.video_reader import Mockup_Video_Reader

eventlet.monkey_patch()


apiBaseUrl = "/animus/"
testApiBaseUrl = apiBaseUrl + "test/"
app_folder = "./client/dist/wizard-of-oz-interface"

app = Flask(__name__, static_url_path="", static_folder=app_folder)
app.config['MONGODB_SETTINGS'] = {
    'db': 'woz_db',
    'host': '127.0.0.1',
    'port': 27017
}
CORS(app)
socketio = SocketIO(app, logger=True, engineio_logger=True)

# Database initialisation
db = MongoEngine()
db.init_app(app)

def get_db_ref():
    return db

from db_setup import User, Project

user_by_email = {}
user_email_by_session_id = {}
video_streamer = None


def build_anguar():
    cmds = ["cd client", "ng build"]
    encoding = "latin1"
    p = subprocess.Popen(
        "cmd.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    for cmd in cmds:
        p.stdin.write((cmd + "\n").encode(encoding))
    p.stdin.close()
    p.wait()


def writeClientConfig(port):
    with open("./client/src/environments/config.json", "w") as json_file:
        data = {"webSocketPort": port}
        json.dump(data, json_file)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters["regex"] = RegexConverter


def get_user_from_cookie() -> Animus_User:
    username = request.cookies.get("ANM_SDK_SESSION", None)
    user = None if not username else user_by_email.get(username)

    return user

def revoke_user_cookie() -> bool:
    try:
        value = request.cookies.get("ANM_SDK_SESSION",None)
        if value: 
            request.cookies.pop("ANM_SDK_SESSION")
    except Exception as e:
        print("Error logout", exc_info=e)
        return False
    
    print("Logged out successfully")
    return True


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers["Cache-Control"] = "public, max-age=0"
    return r


@app.errorhandler(404)
def handle_angular_routes(e):
    return send_from_directory(app_folder, "index.html")


@app.route("/")
def angular():
    return send_from_directory(app_folder, "index.html")


@app.route("/<regex('\w\.(js|css)'):path>")
def angular_src(path):
    return send_from_directory(app_folder, path)


@app.route(apiBaseUrl + "connect", methods=["POST"])
def connect():
    user = get_user_from_cookie()
    if not user:
        return get_missing_user_response()

    chosen_robot = request.json
    robot_id = chosen_robot["robotId"] if chosen_robot else None
    try:
        outcome = user.connect_to_selected_robot(robot_id)
        if not outcome["success"]:
            return get_failure_response(outcome["description"])
    except Exception as e:
        print("connect - Error connecting to robot: ", e)
        return get_failure_response("No robot details were provided")

    return get_success_response("Successfully Connected")


@app.route(apiBaseUrl + "robots")
def get_robots():
    user = get_user_from_cookie()

    if not user:
        return get_missing_user_response()
    else:
        robots, errors = user.get_available_robots()
        success = errors.count != 2

        if success:
            return get_success_response("Success", {"robots": robots, "errors": errors})
        else:
            return get_failure_response("Failure", {"robots": robots, "errors": errors})


@app.route(apiBaseUrl + "check-authenticated")
def check_authenticated():
    user = get_user_from_cookie()

    if not user:
        return get_missing_user_response()
    else:
        response_user = Server_User(user.username).__dict__
        return get_success_response("User Authenticated", response_user)


@app.route(apiBaseUrl + "login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]

    if not user_by_email.get(username):
        user = Animus_User(username)
        outcome = user.login(username, password)

        if outcome["success"]:
            user_by_email[username] = user
            response_user = Server_User(username).__dict__
            login_response = get_success_response("Logged in", response_user)
            login_response.set_cookie(
                "ANM_SDK_SESSION", username, max_age=60 * 60 * 24 * 1
            )
            return login_response
        else:
            return get_failure_response(outcome["description"])
    else:
        return get_failure_response("User already logged in")


@app.route(apiBaseUrl + "logout")
def logout():
    user = get_user_from_cookie()

    if user:
        user.logout()
        user_by_email[user.username] = None

    return get_success_response("Logged out")

@app.route(apiBaseUrl + "save-project", methods=["POST"])
def save_project():
    print("***Saving project started ...")
    user = get_user_from_cookie()

    if user:
        print("*******User Found, checking body")
        if request.json:
            print("*******body Found:", request.json)
            project = Project(
                user=user,
                title=request.json.get('title'),
                description=request.json('description'),
                supportedRobots=request.json('supportedRobots')
            )
            project.save()
        else:
            print("*******no body found")
            return get_failure_response("No project was provided")
    else:
        print("*******no user found")
        return get_missing_user_response()

    return get_success_response("Project saved")

@app.route(apiBaseUrl + "get-projects")
def get_projects(projectId=None):
    user = get_user_from_cookie()

    if user:
        projects = []
        if (projectId):
            projects = Project.objects(username=user, id=projectId).first()
        else:
            projects = Project.objects(username=user)
    
    return get_success_response("Retreived Projects", projects)

@app.route(apiBaseUrl + "say", methods=["POST"])
def say():
    user = get_user_from_cookie()

    if not user:
        return get_missing_user_response()
    else:
        message = request.json.get("message")
        emotion = request.json.get("emotion")
        outcome = user.animus_wrapper.say(message, emotion)

        if outcome["success"]:
            return get_success_response("Message spoken")
        else:
            return get_failure_response(outcome["description"])


@app.route(apiBaseUrl + "start_video_feed")
def start_video_feed():
    user = get_user_from_cookie()
    if user:
        generator = user.animus_wrapper.start_video_stream()
        return Response(
            generator(),
            mimetype="multipart/x-mixed-replace; boundary=frame",
        )
    else:
        return get_missing_user_response()


@app.route(apiBaseUrl + "stop_video_feed")
def stop_video_feed():
    user = get_user_from_cookie()

    if not user:
        return get_missing_user_response()
    else:
        user.animus_wrapper.stop_video_stream()
        return get_success_response("Video Feed Stopped")


@app.route(testApiBaseUrl + "start_video_feed")
def start_mockup_video_feed():
    global video_streamer
    video_streamer = Mockup_Video_Reader()
    video_streamer.capture = True

    return Response(
        video_streamer.start_capture(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


@app.route(testApiBaseUrl + "stop_video_feed")
def stop_mockup_video_feed():
    global video_streamer
    video_streamer.capture = False
    return get_success_response("Video feed stopped")


@socketio.on("connect")
def on_connect():
    username = request.args.get("username")
    print(f"Received connect for sid: {request.sid}, user: {username}")
    user_email_by_session_id[request.sid] = "ms414@hw.ac.uk"
    emit("log", "Connected")


@socketio.on("move_robot")
def on_message_received(msg):
    print("Received message" + json.dumps(msg))
    username = user_email_by_session_id.get(request.sid)
    resp_body = None

    if not username:
        resp_body = get_failure_response_body(f"No session with id: {request.sid}")

    user = user_by_email.get(username)
    if user:
        if msg:
            user.animus_wrapper.move_robot_body(msg["forward"], msg["left"], msg["rotate"])
            resp_body = get_success_response_body("OK")
        else:
            resp_body = get_failure_response_body("No commands provided")
    else:
        resp_body = get_failure_response_body(f"User {username} not connected")

    emit("move_robot", resp_body)


# Clean up any subscription, close any connection open and so on
@atexit.register
def clean_up():
    for username, user in user_by_email.items():
        user.logout()

    print("Cleaned up!!!")


if __name__ == "__main__":
    debug = False
    port = 5000 + random.randint(0, 999)

    writeClientConfig(port)
    # build_anguar()  # Build the client before serving it
    # Don't opens the browser when in debug mode, as url and ports weirdnesses start happening.
    if not debug:
        Timer(0.5, lambda: open_browser(port)).start()

    socketio.run(app, port=port)
