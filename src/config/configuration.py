from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    OPENAI_TOKEN: str = Field(..., env="OPENAI_TOKEN")
    OPENAI_ORGID: str = Field(..., env="OPENAI_ORGID")
    DEBUG: bool = Field(..., env="DEBUG")


settings = Settings()
