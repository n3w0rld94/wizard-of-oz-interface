import sys

sys.path.insert(0, "..")
import atexit
import json
import random
import webbrowser
from threading import Timer

from flask import Flask, Response, request, send_from_directory
from werkzeug.routing import BaseConverter

from models.user_status import Animus_User

apiBaseUrl = "/animus/"
port = 5000 + random.randint(0, 999)
app_folder = "./client/dist/wizard-of-oz-interface"
app = Flask(__name__, static_url_path="", static_folder=app_folder)
user_by_email = {}


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
    json_response = json.dumps(
        {
            "success": success,
            "description": description,
            "code": code,
            "payload": payload,
        }
    )

    resp = Response(json_response, content_type="application/json; charset=utf-8")
    resp.headers.add("content-length", len(json_response))
    resp.status_code = 200

    return resp


@app.route("/")
def angular():
    return send_from_directory(app_folder, "index.html")


@app.route("/<regex('\w\.(js|css)'):path>")
def angular_src(path):
    return send_from_directory(app_folder, path)


@app.route(apiBaseUrl + "connect")
def connect():
    return "Hello World!"


@app.route(apiBaseUrl + "robots")
def get_robots():
    user = get_user_from_cookie()

    if not user:
        return get_response(False, "User not logged in", -1)
    else:
        robots = user.get_available_robots()
        return get_response(True, "success", 1, robots)


@app.route(apiBaseUrl + "check-authenticated")
def check_authenticated():
    user = get_user_from_cookie()
    code = 1 if user != None else -1

    resp = get_response(user != None, "User Authenticated", code)
    return resp


@app.route(apiBaseUrl + "login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    if not user_by_email.get(username):
        user = Animus_User(username)
        login_outcome = user.login(username, password)

        login_response = get_response(
            login_outcome.success, login_outcome.description, login_outcome.code
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


# opens a web browser at the right address
def open_browser():
    webbrowser.open("http://127.0.0.1:" + str(port) + "/")


# Clean up any subscription, close any connection open and so on
@atexit.register
def clean_up():
    for username, user in user_by_email.items():
        user.logout()

    print("cleaned up!!!")


if __name__ == "__main__":
    debug = False

    # Don't opens the browser when in debug mode, as url and ports weirdnesses start happening.
    if not debug:
        Timer(0.5, lambda: open_browser()).start()

    app.run(port=port, debug=debug)

if __name__ == "__main__" and __package__ is None:
    from os import path, sys

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
