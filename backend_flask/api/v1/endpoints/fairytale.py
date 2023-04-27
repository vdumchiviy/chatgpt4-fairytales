from flask import Blueprint, jsonify, request

from backend.chatgpt.fairytale import request_new_fairytale
from backend.chatgpt.models import request_list_models
from backend.schemas.fairytale import FairyTaleStory

# from schemas.fairytale import FairyTaleSetup, FairyTaleStory

fairytale = Blueprint('fairytale', __name__)


@fairytale.route("/models")
async def get_list_models():
    models = jsonify({"models": request_list_models()})
    return models


@fairytale.route("/new")
async def get_new_fairytale():
    hero: str = request.args.get("hero", default="Misha")
    trend: str = request.args.get("trend", default="mercy")
    language: str = request.args.get("language", default="English")
    # ) -> FairyTaleStory:
    result: FairyTaleStory = await request_new_fairytale(
        hero=hero,
        trend=trend,
        language=language
    )
    return jsonify(result.dict())
