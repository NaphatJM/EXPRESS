from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(prefix="/v1/items", tags=["items"])


class Item(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    description: str
    weight_kg: float
    is_fragile: bool = False
    delivery_type: str = "standard"


@router.get("/{item_id}")
def read_item(item_id: int):
    # Mock return of an item
    return {
        "id": item_id,
        "sender_id": 1,
        "receiver_id": 2,
        "description": "Sample item",
        "weight_kg": 1.5,
        "is_fragile": False,
        "delivery_type": "standard",
    }


@router.post("")
def create_item(item: Item):
    return item


@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": f"Item with ID {item_id} has been updated", "item": item}


@router.delete("/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item with ID {item_id} has been deleted"}
