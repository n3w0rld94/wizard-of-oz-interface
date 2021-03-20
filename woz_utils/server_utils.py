import json
import webbrowser

from flask import Response


def get_missing_user_response():
    return get_failure_response("User not logged in")


def get_success_response(message, payload=None):
    return get_response(True, message, 1, payload)


def get_failure_response(message, payload=None):
    return get_response(False, message, -1, payload)


def get_response(success, description, code, payload=None):
    dictionary = dict(
        success=success, description=description, code=code, payload=payload
    )
    json_response = json.dumps(dictionary)

    resp = Response(json_response, content_type="application/json; charset=utf-8")
    resp.headers.add("content-length", len(json_response))
    resp.status_code = 200


def get_failure_response_body(message: str, payload=None):
    return dict(success=False, description=message, code=-1, payload=payload)


def get_success_response_body(message: str, payload=None):
    return dict(success=True, description=message, code=1, payload=payload)


def get_missing_robot_response_body():
    return get_failure_response_body("No robot selected")


def get_unopened_modality_response_body(modality_name):
    return get_failure_response_body(f"Unable to open {modality_name} modality.")


# Opens a web browser at the right address
def open_browser(port):
    webbrowser.open("http://127.0.0.1:" + str(port) + "/")
