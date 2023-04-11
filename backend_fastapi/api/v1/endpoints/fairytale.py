import openai
from config.configuration import settings
from fastapi import APIRouter
from schemas.fairytale import FairyTaleSetup, FairyTaleStory

router = APIRouter()


@router.get(path="/models")
async def get_list_models():
    openai.organization = settings.OPENAI_ORGID
    openai.api_key = settings.OPENAI_TOKEN
    models = openai.Model.list()
    return models


@router.get(path="/new", response_model=FairyTaleStory)
async def create_new_fairytale(
    hero: str = "Misha",
    trend: str = "mercy",
    language: str = "English"
) -> FairyTaleStory:
    fairytale_request = FairyTaleSetup(
        hero=hero, trend=trend, language=language)
    openai.organization = settings.OPENAI_ORGID
    openai.api_key = settings.OPENAI_TOKEN

    completion_resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": f"Tell a short story in {language}. Heroes - "
                + f"{hero}. A fairy tale should teach {trend}."}
        ],
    )
    story = completion_resp["choices"][0]["message"]["content"]
    result_dict = dict(fairytale_request)
    result_dict.update({"story": story})
    return FairyTaleStory(**result_dict)
