from flask import Blueprint, jsonify

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
async def get_new_fairytale(
    hero: str = "Misha",
    trend: str = "mercy",
    language: str = "English"
):
    # ) -> FairyTaleStory:
    result: FairyTaleStory = await request_new_fairytale(
        hero=hero,
        trend=trend,
        language=language
    )
    return jsonify(result.dict())
