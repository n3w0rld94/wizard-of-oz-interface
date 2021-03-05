import threading
from flask import Flask
from flask import send_from_directory
from werkzeug.routing import BaseConverter
import webbrowser, random, atexit, os
from threading import Timer

apiBaseUrl = "/animus/"
port = 5000 + random.randint(0, 999)
app = Flask(
    __name__, static_url_path="", static_folder="../client/dist/wizard-of-oz-interface"
)


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


# opens a web browser at the right address
def open_browser():
    webbrowser.open("http://127.0.0.1:" + str(port) + "/")


# Clean up any subscription, close any connection open and so on
@atexit.register
def clean_up():
    print("cleaned up!!!")


if __name__ == "__main__":
    debug=False
    
    # Don't opens the browser when in debug mode, as url and ports weirdnesses start happening.
    if not debug:
        Timer(0.5, lambda: open_browser()).start()
    
    app.run(port=port, debug=debug)
    
