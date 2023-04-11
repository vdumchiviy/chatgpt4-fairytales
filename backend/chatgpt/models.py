import openai

# from config.configuration import settings
from backend.config.configuration import settings

# from schemas.fairytale import FairyTaleSetup, FairyTaleStory


def request_list_models():
    openai.organization = settings.OPENAI_ORGID
    openai.api_key = settings.OPENAI_TOKEN
    models = openai.Model.list()
    return models
