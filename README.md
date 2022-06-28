# keywords_api

Get and Store data with keywords_api. <br /> REST API service for storing keywords
from the daily events traffic and display useful data about them.<br />

This API written in Python and use FastApi Framework.

## Install

    pip install fastapi

    pip install uvicorn

### Run the app

    uvicorn src.main:app --reload

### Docker Install

    docker build -t keywords-task:latest .
   
    docker run -d -p 8000:80 keywords-task

<br/>


### Request

post new event.

`POST //events`

    curl -X POST http://localhost:8000/events -d "Checkpoint and Avanan is leading in cyber security products."

Important: the data after flag (-d) need to be wrapped in double-quoted.

<br/>

### Response

    content-length: 16 
    content-type: application/json 
    date: Tue,28 Jun 2022 10:23:16 GMT 
    server: uvicorn 
    x-process-time: 0.001127004623413086 

    "event received"



### Request

Get Json with the number occurrence of specific keywords in the received interval time.

currently, api supported keywords: "checkpoint", "avanan", "email", "security"

note: if some keyword not inserted at all in given interval, the keyword will not be in the Json result.

Get 

`GET /stats?interval=<int>`

    curl http://localhost:8000/stats?interval=60

### Response

     content-length: 27 
     content-type: application/json 
     date: Tue,28 Jun 2022 10:31:51 GMT 
     server: uvicorn 
     x-process-time: 0.0025954246520996094 

    {
      "checkpoint": 1,
      "avanan": 1
    }
