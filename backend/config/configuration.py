from typing import Any, Dict
import os
from pydantic import BaseSettings, Field

server_info: Dict[str, Any] = {
    "version": "1.1",
    "last_date": "2023-04-11",
    "code": 200,
    "msg": "OK"
}

cur_dir = os.path.abspath(os.path.dirname(__file__))

class Settings(BaseSettings):
    OPENAI_TOKEN: str = "n"
    OPENAI_ORGID: str = "h"
    DEBUG: bool = True

    class Config:
        env_file = [os.path.join(cur_dir, ".env")]


settings = Settings()  # type: ignore[call-arg]
print(settings.OPENAI_ORGID)