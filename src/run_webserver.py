from fastapi import FastAPI
from src.api.v1.api import api_router

app = FastAPI(debug=True)

app.include_router(router=api_router, prefix="")
