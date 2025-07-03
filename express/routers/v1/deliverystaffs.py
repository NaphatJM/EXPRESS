from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/v1/deliverystaffs", tags=["deliverystaffs"])


class DeliveryStaff(BaseModel):
    id: int
    name: str
    phone: str
    current_location: str
    is_active: bool = True


@router.get("/{staff_id}")
def read_deliverystaff(staff_id: int):
    return DeliveryStaff(
        id=staff_id,
        name="John Doe",
        phone="1234567890",
        current_location="Bangkok",
        is_active=True,
    )


@router.post("")
def create_deliverystaff(staff: DeliveryStaff):
    return staff


@router.put("/{staff_id}")
def update_deliverystaff(staff_id: int, staff: DeliveryStaff):
    return staff


@router.delete("/{staff_id}")
def delete_deliverystaff(staff_id: int):
    return {"message": f"DeliveryStaff with id {staff_id} deleted"}
