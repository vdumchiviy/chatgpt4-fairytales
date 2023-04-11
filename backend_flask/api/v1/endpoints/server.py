from flask import Blueprint, jsonify
from backend.config.configuration import server_info

server = Blueprint('server', __name__)


@server.route("/info")
def get_server_short_info():
    result = jsonify(server_info)
    return result
