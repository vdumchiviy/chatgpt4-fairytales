from flask import Blueprint, jsonify
# from backend.config.configuration import server_info
from backend.server.server import get_server_info
from backend.schemas.server import ServerShortInfo

server = Blueprint('server', __name__)


@server.route("/info")
async def get_server_short_info():
    server_info: ServerShortInfo = get_server_info()
    result = jsonify(server_info.dict())
    return result
