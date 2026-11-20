from enum import StrEnum
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/items/{itme_id}")
async def read_itme(itme_id : int):
    return {"itme_id": itme_id}

