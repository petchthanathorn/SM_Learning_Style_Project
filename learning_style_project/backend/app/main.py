from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "description": item.description}
