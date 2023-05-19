import os

from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

os.makedirs("data/", exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    with open(os.path.join("data/", filename), "wb") as buffer:
        buffer.write(await file.read())


@app.post("/uploadHash/{new_hash}")
async def upload_hash(new_hash: str):
    print(new_hash)
    with open(os.path.join("data/", "new_hash.txt"), "a") as f:
        f.write(new_hash)
