from pydantic import BaseModel


class ServerShortInfo(BaseModel):
    version: str
    last_date: str
    msg: str
