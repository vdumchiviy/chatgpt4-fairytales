from backend.config.configuration import server_info
from backend.schemas.server import ServerShortInfo


def get_server_info() -> ServerShortInfo:
    return ServerShortInfo(**server_info)
