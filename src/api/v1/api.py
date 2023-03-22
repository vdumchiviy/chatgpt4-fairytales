from fastapi import APIRouter
from .endpoints import server

api_router = APIRouter()


api_router.include_router(server.router, prefix='/server')