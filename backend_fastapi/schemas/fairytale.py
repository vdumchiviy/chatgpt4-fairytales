from pydantic import BaseModel


class FairyTaleSetup(BaseModel):
    hero: str
    trend: str
    language: str


class FairyTaleStory(FairyTaleSetup):
    story: str
