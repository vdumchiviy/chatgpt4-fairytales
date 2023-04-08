from fastapi import APIRouter

from schemas.server import ServerShortInfo

router = APIRouter()


@router.get("/info", response_model=ServerShortInfo)
async def get_server_short_info() -> ServerShortInfo:
    result = ServerShortInfo(version="1.0", last_date="2023-03-23", code=200, msg="OK")
    return result
