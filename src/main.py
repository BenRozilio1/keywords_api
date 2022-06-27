import datetime

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.db import Database
from src.services import handle_event

app = FastAPI()
db = Database()


class Event(BaseModel):
    created: float = Field(default_factory=datetime.datetime.now().timestamp)
    text: str


@app.post("/events", status_code=201)
def events(event: Event):
    text = event.text
    data = handle_event(text)
    db.insert(event.created, data)
    return data


@app.get("/stats/{interval:int}", status_code=200)
def stats(interval: int):
    result = db.query(interval)
    return result


if __name__ == '__main__':
    uvicorn.run(app, port=8000, debug=True)
