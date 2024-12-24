"""
First steps example from FastAPI docs.
https://fastapi.tiangolo.com/tutorial/first-steps/
"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    """Home page. """
    return {"message": "Hello World"}
