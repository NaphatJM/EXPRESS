from fastapi import FastAPI, Request
from express.routers.v1 import items

app = FastAPI()
app.include_router(items.router, prefix="/v1")
# we can prefix both either main or routers , even tag=[''] is writeable


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
