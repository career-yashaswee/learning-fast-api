from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

db = {
    1245: {"weight": 0.5, "title": "Hello Ladies 2", "status": "OUT_OF_STOCK"},
    1246: {"weight": 0.5, "title": "Hello Ladies 90", "status": "OUT_OF_STOCK"},
    1247: {"weight": 0.5, "title": "Hello Ladies 233", "status": "OUT_OF_STOCK"},
}


@app.post("/books")
def submit_books(weight: int, title: str, statuss: str) -> dict[str, int]:
    if weight > 25:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)

    new_id = max(db.keys()) + 1
    db[new_id] = {"weight": weight, "title": title, "status": statuss}
    return {"id": new_id}


# def submit_books(weight: int, data:dict) -> dict[str, Any]:
#     content = data['content']
#     title = data['title']
#     return {
#         "weight": weight,
#         "content" : content,
#         "title" : title
#     }

@app.put("/books/")
def update_books(id: int, content: str, weight: str, statuss: str) -> dict[str,Any]:
    return {
          "weight": weight,
        "content" : content,
        "statuss" : statuss,
    }



@app.get("/books/latest")
def get_latest_books():
    return db[max(db.keys())]


@app.get("/books")
def get_books(id: int | None = None) -> dict[str, Any]:
    if not id:
        id = max(db.keys())
        return db[id]

    if id not in db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")

    return db[id]


@app.put("/books")
def shipment_update(id: int, content: str, weight: int, statuss: str):
    db[id] = {}


# @app.patch("/books")
# def patch_books(id:int, data:dict[str,Any]):
#     record = db[id]
#     record.update(data)
#     db[id] = record
#     return record


@app.delete("/books")
def delete_books(id:int) -> dict[str,Any]:
    db.pop(id)
    return {
        "details" : "The Object is Deleted"
    }

@app.get("/books/field/{field}")
def get_books_by_field(field: str, id: int):
    return db[id][field]


@app.get("/my-docs", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="My Docs")
