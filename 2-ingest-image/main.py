"""
Example code for ingesting and returning images.
"""
from io import BytesIO
from typing import Tuple
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from PIL import Image
from pydantic import BaseModel


app = FastAPI()


class Addends(BaseModel):
    addend1: int
    addend2: int


class ImageBytes(BaseModel):
    mode: str              # ex: RGB
    size: Tuple[int, int]  # width x height
    data: str


@app.get("/")
async def root():
    """Home page. """
    return {"message": "Hello World"}


@app.post("/add/")
async def add(to_add: Addends):
    """Add integers together. """
    return to_add.addend1 + to_add.addend2


@app.post("/reshape/")
async def reshape(to_reshape: ImageBytes):
    """Reshape a flattened image. """
    data = bytes.fromhex(to_reshape.data)  # undo client conversion to hex/str
    img = Image.frombytes(to_reshape.mode, to_reshape.size, data)
    img_io = BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)
    return StreamingResponse(img_io, media_type="image/png")
