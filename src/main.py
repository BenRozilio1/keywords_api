import asyncio
import datetime
import logging
import time

import uvicorn
from fastapi import FastAPI
from requests import Request

from src.db import Database
from src.models import Event
from src.services import handle_event

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
async def events(event: Event):
    logging.info("Event received: %s", event.json())
    text = event.text
    data = await asyncio.to_thread(handle_event, text)
    db.insert(datetime.datetime.now().timestamp(), data)
    return data


@app.get("/stats/{interval:int}", status_code=200)
def stats(interval: int):
    result = db.query(interval)
    return result


if __name__ == '__main__':
    uvicorn.run(app, port=8000, debug=True)
