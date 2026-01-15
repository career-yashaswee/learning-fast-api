from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

db = {
    1245 : {
        "weight" : 0.5,
        "title" : "Hello Ladies 2",
        "status" : "OUT_OF_STOCK"
    },
     1246 : {
        "weight" : 0.5,
        "title" : "Hello Ladies 90",
        "status" : "OUT_OF_STOCK"
    },
     1247 : {
        "weight" : 0.5,
        "title" : "Hello Ladies 233",
        "status" : "OUT_OF_STOCK"
    }
}

@app.post("/books")
# def submit_books(weight:int,title:str,statuss:str) -> dict[str,int]:

#     if weight > 25:
#         raise HTTPException(
#             status_code=status.HTTP_406_NOT_ACCEPTABLE
#         )
    
#     new_id = max(db.keys()) + 1
#     db[new_id] = {
#         "weight" : weight,
#         "title" : title,
#         "status" : statuss
#     }
#     return {
#         "id" : new_id
#     }
def submit_books(weight: int, data:dict) -> dict[str, Any]:
    content = data['content']
    title = data['title']
    return {
        "weight": weight,
        "content" : content,
        "title" : title
    }


@app.get("/books/latest")
def get_latest_books():
    return db[max(db.keys())]

@app.get("/books")
def get_books(id:int | None = None ) -> dict[str,Any]:
    
    if not id:
        id = max(db.keys())
        return db[id]
    
    if id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="not found"
        )
    
    return db[id]

@app.get("/my-docs",include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="My Docs"
    )