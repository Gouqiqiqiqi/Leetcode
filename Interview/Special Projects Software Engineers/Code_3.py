from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session

app = FastAPI()
engine = create_engine("sqlite:///./test.db")
SQLModel.metadata.create_all(engine)

class Item(SQLModel, table=True):  # data model for items
    id: int = Field(default=None, primary_key=True)
    name: str
    tags: list[str] = []

@app.post("/items/")  # create a new item
def create_item(name: str, tags: list[str] = []):
    item = Item(name=name, tags=tags)
    with Session(engine) as session:
        session.add(item); session.commit(); session.refresh(item)
    return item

@app.get("/items/{item_id}")  # retrieve an item by ID
def read_item(item_id: int):
    item = Session(engine).get(Item, item_id)
    if not item: raise HTTPException(404, "Not found")
    return item