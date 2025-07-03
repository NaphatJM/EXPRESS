from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/v1/receivers", tags=["reciever"])


# define Pydantic model for request/response body
class Receiver(BaseModel):
    id: int
    name: str
    phone: str
    address: str
    is_active: bool = True


# GET /v1/receivers/{receiver_id}
@router.get("/{receiver_id}")
def read_receiver(receiver_id: int, q: str | None = None) -> Receiver:
    return {
        "name": f"Receiver #{receiver_id}",
        "phone": "0812345678",
        "address": "123 Main St.",
        "is_active": True,
    }


# POST /v1/receivers
@router.post("")
def create_receiver(receiver: Receiver):
    return {"message": "Receiver created", "receiver": receiver}


# PUT /v1/receivers/{receiver_id}
@router.put("/{receiver_id}")
def update_receiver(receiver_id: int, receiver: Receiver):
    return {"message": f"Receiver {receiver_id} updated", "receiver": receiver}


# DELETE /v1/receivers/{receiver_id}
@router.delete("/{receiver_id}")
def delete_receiver(receiver_id: int):
    return {"message": f"Receiver with ID {receiver_id} has been deleted"}
