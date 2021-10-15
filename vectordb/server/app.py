from fastapi import FastAPI, Response, Request
from pydantic import BaseModel
from typing import Any
import msgpack_numpy as msgpack_np
from msgpack_asgi import MessagePackMiddleware
class InsertRequest(BaseModel):
    key: str
    data: str

app = FastAPI()

app.add_middleware(MessagePackMiddleware)

@app.get("/")
async def hello():
    return {"message": "Hello World"}

@app.post("/insert")
async def insert(request: Request):

    return Response("ss", status_code=201)

