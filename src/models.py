import datetime

from pydantic import BaseModel, PrivateAttr


class Event(BaseModel):
    text: str