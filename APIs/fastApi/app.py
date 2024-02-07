from fastapi import FastAPI 
from typing import Union 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Olá, mundo!"}

@app.get("/item/{item.id}")
async def read_item(item_id: int, busca: Union[str, int] = None):
    return {"item_id": item_id, "busca": busca}