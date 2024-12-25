"""
Example code for accepting POST request data.
"""
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Addends(BaseModel):
    addend1: int
    addend2: int


@app.get("/")
async def root():
    """Home page. """
    return {"message": "Hello World"}


@app.post("/add/")
async def add(to_add: Addends):
    """Add integers together. """
    return to_add.addend1 + to_add.addend2
