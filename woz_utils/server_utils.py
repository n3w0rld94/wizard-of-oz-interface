import json

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
    return dict(
        success=False,
        description=message,
        code=-1,
        payload=payload
    )

def get_success_response_body(message: str, payload=None):
    return dict(
        success=True,
        description=message,
        code=1,
        payload=payload
    )