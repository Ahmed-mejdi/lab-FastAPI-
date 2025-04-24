from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create an app
app = FastAPI()

# Create a data storage
items = []

# Define a model for our items
class Item(BaseModel):
    text: str
    is_done: bool = False

# Define root endpoint
@app.get("/")
def root():
    return {"Hello": "World"}

# Create a new item
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item

# Get a specific item by ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# List items with optional limit
@app.get("/items/", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]
