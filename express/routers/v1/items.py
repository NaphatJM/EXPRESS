from pydantic import BaseModel
from fastapi import APIRouter  #!!!

router = APIRouter(prefix="/items", tags=["items"])
# we can use prefix to prefixed the url path


class Item(BaseModel):
    name: str
    cost: float
    is_offer: bool = False


# change @app to @router
@router.get("/{item_id}")
async def read_item(item_id: int, q: str | None = None) -> Item:
    return {"item_id": item_id, "q": q}


@router.post("")
async def create_item(item: Item):
    return {"item": item}


@router.put("/{item_id}")
async def update_item(item_id: int, item: Item):
    return item


@router.delete("/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item with ID {item_id} has been deleted"}
