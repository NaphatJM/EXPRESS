from fastapi import APIRouter

# just import all everything in items file
from . import items
from . import receivers

router = APIRouter()
# but we use items.router aka thoose @router decoration
router.include_router(items.router, prefix="/layer3")
router.include_router(receivers.router, prefix="/layer3")
