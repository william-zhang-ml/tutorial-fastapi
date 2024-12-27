"""
Dummy server for testing GET and POST requests.
"""
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class PostData(BaseModel):
    """Dummy POST request data format. """
    number: float
    text: str


@app.get("/get/")
async def get():
    """Route for testing GET requests. """
    return {"message": "hello client"}


@app.post("/post/")
async def post(data: PostData):
    """Route for testing POST requests. """
    return {"message": f"received {data.number} and '{data.text}'"}
