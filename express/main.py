from fastapi import FastAPI, Request
from typing import Union

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


# this is how we sent data via parameter
@app.get("/items/{item_id}")
def read_param(item_id: int):
    return {"item_id": item_id}


# this is how we sen data via query string
@app.get("/imgs/{img_id}")
# we use Union for optional value, like it can be null by default
def read_query(img_id: int, q: Union[str, None] = None):
    return {"img_id": img_id, "q": q}  # GET: 127.0.0.1:8000/imgs/5/?q=hello


@app.post("/items")
# when we use request we have to import Request class and function have to async
async def post_item(req: Request):
    body = await req.json()  # json() convert json into dictionary name "body"
    print(body["name"])  # show in console
    return {"body": body}  # we return dict name "body"
