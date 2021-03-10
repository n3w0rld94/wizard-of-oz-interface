import sys

sys.path.insert(0, "..")

from flask import Flask, send_from_directory, request, Response
import json
from werkzeug.routing import BaseConverter
import webbrowser, random, atexit, os
from threading import Timer

from animus.animus_wrapper.animus_wrapper import Animus_Client


apiBaseUrl = "/animus/"
port = 5000 + random.randint(0, 999)
app = Flask(
    __name__, static_url_path="", static_folder="../client/dist/wizard-of-oz-interface"
)

animus_client = Animus_Client()


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters["regex"] = RegexConverter


@app.route("/")
def angular():
    return send_from_directory("../client/dist/wizard-of-oz-interface", "index.html")


@app.route("/<regex('\w\.(js|css)'):path>")
def angular_src(path):
    return send_from_directory("../client/dist/wizard-of-oz-interface", path)


@app.route(apiBaseUrl + "connect")
def hello():
    return "Hello World!"


@app.route(apiBaseUrl + "login")
def login(path):
    username = request.args.get("username")
    password = request.args.get("password")

    login_outcome = animus_client.login(username, password)

    json_response = json.dumps(login_outcome)
    login_response = Response(
        json_response, content_type="application/json; charset=utf-8"
    )
    login_response.headers.add("content-length", len(json_response))
    login_response.status_code = 200

    return login_response


# opens a web browser at the right address
def open_browser():
    webbrowser.open("http://127.0.0.1:" + str(port) + "/")


# Clean up any subscription, close any connection open and so on
@atexit.register
def clean_up():
    animus_client.dispose_animus()
    print("cleaned up!!!")


if __name__ == "__main__":
    debug = False

    # Don't opens the browser when in debug mode, as url and ports weirdnesses start happening.
    if not debug:
        Timer(0.5, lambda: open_browser()).start()

    app.run(port=port, debug=debug)

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
