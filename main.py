import atexit
from collections import namedtuple
import json
import random
import subprocess
import webbrowser
from threading import Timer
from woz_utils.proto_converters import dictToSnakeCaseObject

import eventlet
from flask import Flask, Response, request, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO, emit

from woz_utils.server_user import Server_User
from woz_utils.video_reader import Mockup_Video_Reader

eventlet.monkey_patch()

from werkzeug.routing import BaseConverter

from models.user_status import Animus_User

apiBaseUrl = "/animus/"
testApiBaseUrl = apiBaseUrl + "test/"
app_folder = "./client/dist/wizard-of-oz-interface"

app = Flask(__name__, static_url_path="", static_folder=app_folder)
CORS(app)
socketio = SocketIO(app, logger=True, engineio_logger=True)
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


def get_response(success, description, code, payload=None):
    dictionary = dict(
        success=success, description=description, code=code, payload=payload
    )
    json_response = json.dumps(dictionary)

    resp = Response(json_response, content_type="application/json; charset=utf-8")
    resp.headers.add("content-length", len(json_response))
    resp.status_code = 200

    return resp


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
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
        return get_response(False, "User not logged in", -1)

    try:
        chosen_robot = request.json
        print("connection robot " + json.dumps(chosen_robot))
        if not chosen_robot:
            return get_response(False, "No robot details were provided", -1)

        outcome = user.connect_to_selected_robot(chosen_robot['robotId'])

        print("outcome", outcome)

        if not outcome["success"]:
            return get_response(False, outcome["description"], outcome["code"])
    except Exception as e:
        print("error connecting", e)
        return get_response(False, "No robot details were provided", -1)

    success_response = get_response(True, "Successfully Connected", 1)
    return success_response


@app.route(apiBaseUrl + "robots")
def get_robots():
    user = get_user_from_cookie()

    if not user:
        return get_response(False, "User not logged in", -1)
    else:
        robots, errors = user.get_available_robots()
        success = errors.count != 2
        code = 1 if success else -1
        description = "Succeeded" if success else "Failed"
        return get_response(
            success, description, code, {"robots": robots, "errors": errors}
        )


@app.route(apiBaseUrl + "check-authenticated")
def check_authenticated():
    user = get_user_from_cookie()
    user_is_authenticated = user != None
    code = 1 if user_is_authenticated else -1

    response_user = (
        Server_User(user.username).__dict__ if user_is_authenticated else None
    )

    resp = get_response(
        user_is_authenticated, "User Authenticated", code, response_user
    )
    return resp


@app.route(apiBaseUrl + "login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if not user_by_email.get(username):
        user = Animus_User(username)
        login_outcome = user.login(username, password)
        response_user = (
            Server_User(username).__dict__ if login_outcome.success else None
        )

        login_response = get_response(
            login_outcome.success,
            login_outcome.description,
            login_outcome.code,
            response_user,
        )

        if login_outcome.success:
            login_response.set_cookie(
                "ANM_SDK_SESSION", username, max_age=60 * 60 * 24 * 7
            )
            user_by_email[username] = user

        return login_response
    else:
        return get_response(False, "User already logged in", -1)


@app.route(apiBaseUrl + "logout")
def logout():
    user = get_user_from_cookie()

    if user:
        user.logout()
        user_by_email[user.username] = None

    return get_response(True, "User logged out successfully", 1)


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
        return


@app.route(apiBaseUrl + "stop_video_feed")
def stop_video_feed():
    user = get_user_from_cookie()

    if user:
        user.animus_wrapper.stop_video_stream()

    resp = get_response(True, "Video Feed Stopped", 1)
    return resp


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
    resp = get_response(True, "Video Feed Stopped", 1)
    return resp


@socketio.on("connect")
def on_connect():
    username = request.args.get("username")
    print("received connect for " + request.sid)
    print("received connect for " + username)
    user_email_by_session_id.set(request.sid, username)
    emit("log", "Connected", broadcast=True)


@socketio.on("move_robot")
def on_message_received(msg):
    print("received message" + json.dumps(msg))
    username = user_email_by_session_id.get(request.sid)

    if username:
        user = user_by_email.get(username)
        if user:
            user.animus_wrapper.move_robot_body(msg.forward, msg.left, msg.rotate)
            emit("move_robot", {"message": "OK", "success": True})
        else:
            emit(
                "move_robot",
                {
                    "message": "no user found with username: " + username,
                    "success": False,
                },
            )
    else:
        emit(
            "move_robot",
            {
                "message": "no username found with session id: " + request.sid,
                "success": False,
            },
        )


# opens a web browser at the right address
def open_browser(port):
    webbrowser.open("http://127.0.0.1:" + str(port) + "/")


# Clean up any subscription, close any connection open and so on
@atexit.register
def clean_up():
    for username, user in user_by_email.items():
        user.logout()

    print("cleaned up!!!")


if __name__ == "__main__":
    debug = False
    port = 5000 + random.randint(0, 999)

    writeClientConfig(port)
    # build_anguar()  # Build the client before serving it
    # Don't opens the browser when in debug mode, as url and ports weirdnesses start happening.
    if not debug:
        Timer(0.5, lambda: open_browser(port)).start()

    socketio.run(app, port=port)
