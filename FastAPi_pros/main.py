from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# Example data storage (you can use a database in a real application)
items = []


class Item(BaseModel):
    item_id: int
    q: Union[str, None] = None


@app.get("/")
async def read_root():
    return FileResponse("templates/fastapi_pro1.html")


@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item created successfully"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item.item_id == item_id:
            return item.dict()
    return {"message": "Item not found"}
