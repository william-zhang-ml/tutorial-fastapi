"""
Dummy server for testing GET and POST requests.
https://fastapi.tiangolo.com/tutorial/response-model/
"""
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class ResponseData(BaseModel):
    """Dummy POST request data format. """
    number: float
    text: str
    flag: bool


@app.get("/get/")
async def get():
    """Route for testing GET requests. """
    return ResponseData(number=1, text='a', flag=True)
