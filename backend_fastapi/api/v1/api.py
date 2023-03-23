from fastapi import APIRouter
from .endpoints import server, fairytale

api_router = APIRouter()


api_router.include_router(server.router, prefix='/server')
api_router.include_router(fairytale.router, prefix='/fairytale')
