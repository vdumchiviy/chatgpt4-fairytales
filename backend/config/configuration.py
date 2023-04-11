from pydantic import BaseSettings, Field
from typing import Dict, Any

server_info: Dict[str, Any] = {
    "version": "1.1",
    "last_date": "2023-04-11",
    "code": 200,
    "msg": "OK"
}


class Settings(BaseSettings):
    OPENAI_TOKEN: str = Field(..., env="OPENAI_TOKEN")
    OPENAI_ORGID: str = Field(..., env="OPENAI_ORGID")
    DEBUG: bool = Field(..., env="DEBUG")


settings = Settings()  # type: ignore[call-arg]
