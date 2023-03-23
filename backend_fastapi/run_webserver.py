from fastapi import FastAPI
from backend_fastapi.api.v1.api import api_router
from backend_fastapi.config.configuration import settings


app = FastAPI(debug=settings.DEBUG)

app.include_router(router=api_router, prefix="")

