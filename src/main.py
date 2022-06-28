import datetime
import logging
import time

import uvicorn
from fastapi import FastAPI, Depends, Request, Form

from src.db import Database
from src.models import Event
from src.services import EventService

logging.basicConfig(level=logging.INFO)
app = FastAPI()
db = Database()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.post("/events", status_code=201)
async def events(request: Request):
    body = await request.body()
    text = body.decode("utf-8")
    logging.info("Event received: %s", text)
    data = EventService.handle_event(text)
    db.insert(datetime.datetime.now().timestamp(), data)
    return "event received"


@app.get("/stats", status_code=200)
def stats(interval: int = 0):
    result = db.query(interval)
    return result


@app.get("/hello", status_code=200)
def hello():
    return "hi"


if __name__ == '__main__':
    uvicorn.run(app, port=8000, debug=True)
