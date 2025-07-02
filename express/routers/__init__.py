from fastapi import APIRouter

# we import routers that has __init__.py that contain router(V1)
from . import v1

# it mean that we can add multiple router in this file or in case of we have multiple version v1,v2,v3 so on

router = APIRouter()
router.include_router(v1.router, prefix="/layer2")
