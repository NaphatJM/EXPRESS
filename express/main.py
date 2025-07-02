from fastapi import FastAPI, Request
from typing import Union

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/items")
async def create_item(item: dict):
    return {"item": item}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item with ID {item_id} has been deleted"}
