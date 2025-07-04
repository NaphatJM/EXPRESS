from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from pydantic import BaseModel

router = APIRouter(prefix="/v1/shipments", tags=["shipments"])


class Shipment(BaseModel):
    id: int
    parcel_id: int
    status: str
    current_location: str
    estimated_delivery: datetime


@router.get(
    "/",
)
@router.get("/{shipment_id}")
def get_shipment(shipment_id: int):
    return {
        "id": shipment_id,
        "parcel_id": 101,
        "status": "in_transit",
        "current_location": "Bangkok",
        "estimated_delivery": datetime(2024, 6, 30, 17, 0),
    }


@router.post("/")
def create_shipment(shipment: Shipment):
    return shipment


@router.put("/{shipment_id}")
def update_shipment(shipment_id: int, shipment: Shipment):
    return {
        "message": f"Shipment with ID {shipment_id} has been updated",
        "shipment": shipment,
    }


@router.delete("/{shipment_id}")
def delete_shipment(shipment_id: int):
    return {"detail": f"Shipment {shipment_id} deleted"}
