from fastapi import FastAPI, Request

# we import routers that has __init__.py that contain router(routers)
from express import routers

app = FastAPI()
app.include_router(routers.router, prefix="/layer1")


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
