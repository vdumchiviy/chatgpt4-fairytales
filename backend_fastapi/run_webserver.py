from fastapi import FastAPI

from api.v1.api import api_router
from config.configuration import settings

app = FastAPI(debug=settings.DEBUG)

app.include_router(router=api_router, prefix="")
