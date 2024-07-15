from fastapi import FastAPI, HTTPException
from database import create_item, read_item, update_item, delete_item

app = FastAPI()

@app.post("/items/")
def create_new_item(item_data: dict):
    new_item_id = create_item(item_data)
    return {"message": "Item created successfully", "item_id": new_item_id}

@app.get("/items/{item_id}")
def read_single_item(item_id: str):
    item = read_item(item_id)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update_existing_item(item_id: str, item_data: dict):
    if update_item(item_id, item_data):
        return {"message": "Item updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_existing_item(item_id: str):
    if delete_item(item_id):
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")