from fastapi import APIRouter

# just import all everything in items file
from . import items, receivers, senders, shipments, deliverystaffs


router = APIRouter()
# but we use items.router aka thoose @router decoration
router.include_router(items.router, prefix="/layer3")
router.include_router(receivers.router, prefix="/layer3")
router.include_router(senders.router, prefix="/layer3")
router.include_router(shipments.router, prefix="/layer3")
router.include_router(deliverystaffs.router, prefix="/layer3")
