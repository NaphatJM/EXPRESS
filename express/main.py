from fastapi import FastAPI, Request

# use pydantic for schema validation
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    cost: float
    is_offer: bool = False


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


#  if you watch following api closely you can see that we use Item(Model) that we created instead of dict
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None) -> Item:
    return {"item_id": item_id, "q": q}


@app.post("/items")
async def create_item(item: Item):
    return {"item": item}


# for example if you not sent body(json) that match schema via request, its will return 422 Error: Unprocessable Entity
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    print(item)
    # return Item(name=item.name, cost=item.cost, is_offer=item.is_offer)
    return item


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item with ID {item_id} has been deleted"}
