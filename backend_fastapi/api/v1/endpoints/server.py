from fastapi import APIRouter
from backend_fastapi.schemas.server import ServerShortInfo


router = APIRouter()


@router.get("/info", response_model=ServerShortInfo)
async def get_server_short_info() -> ServerShortInfo:
    return ServerShortInfo(version="1.0", last_date="2023-03-23", msg="OK")
