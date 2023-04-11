from flask import Blueprint, jsonify

server = Blueprint('server', __name__)


@server.route("/info")
def get_server_short_info():
    result = jsonify(
        {
            "version": "1.0",
            "last_date": "2023-03-23",
            "code": 200,
            "msg": "OK"
        }
    )
    return result
