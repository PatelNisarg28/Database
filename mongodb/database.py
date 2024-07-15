# database.py
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "school"
COLLECTION_NAME = "data"

# MongoDB connection
try:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    print("Connected to MongoDB")
except ConnectionFailure:
    print("Failed to connect to MongoDB")

# CRUD Operations
def create_item(item_data: dict):
    result = collection.insert_one(item_data)
    return result.inserted_id

def read_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item:
        item["_id"] = str(item["_id"])  # Convert ObjectId to string for JSON serialization
    return item

def update_item(item_id: str, item_data: dict):
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": item_data})
    return result.matched_count > 0

def delete_item(item_id: str):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0