from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/v1/senders", tags=["senders"])


class Sender(BaseModel):
    id: int
    name: str
    phone: str
    address: str


# Read one
@router.get("/{sender_id}")
def get_sender(sender_id: int):
    return {
        "id": sender_id,
        "name": "Sample",
        "phone": "0000000000",
        "address": "Sample Address",
    }


# Create
@router.post("/")
def create_sender(sender: Sender):
    return sender


# Update
@router.put("/{sender_id}")
def update_sender(sender_id: int, sender: Sender):
    return sender


# Delete
@router.delete("/{sender_id}")
def delete_sender(sender_id: int):
    return {"message": f"Sender {sender_id} deleted"}
