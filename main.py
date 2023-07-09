import uvicorn
import json
import requests
from typing import List
from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from bson import ObjectId


app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client.get_database("ecommerce")
products_collection = db.get_collection("products")
orders_collection = db.get_collection("orders")


class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str


class Item(BaseModel):
    product_id: str = Field(..., alias="_id")
    bought_quantity: int
    total_amount: float


class Order(BaseModel):
    timestamp: str
    items: List[Item]
    user_address: UserAddress


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/products")
def get_products():
    products = products_collection.find({})
    encoded_products = []
    for product in products:
        product["_id"] = str(product["_id"])
        encoded_products.append(product)
    return JSONResponse(content=encoded_products)


@app.post("/orders")
def create_order(order: Order):
    order_data = order.dict()
    order_data["items"] = [
        {**item.dict(), "_id": ObjectId(item.product_id)} for item in order.items
    ]
    order_id = orders_collection.insert_one(order_data).inserted_id
    return {"order_id": str(order_id)}


@app.get("/orders")
def get_orders(limit: int = 10, offset: int = 0):
    orders = orders_collection.find().skip(offset).limit(limit)
    encoded_orders = []
    for order in orders:
        order_dict = {
            "_id": str(order["_id"]),
            "timestamp": order["timestamp"],
            "items": [
                {**item, "_id": str(item["_id"])}
                for item in order["items"]
            ],
            "user_address": order["user_address"],
        }
        encoded_orders.append(order_dict)
    return JSONResponse(content=encoded_orders)


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    order = orders_collection.find_one({"_id": ObjectId(order_id)})
    if order:
        order_dict = {
            "_id": str(order["_id"]),
            "timestamp": order["timestamp"],
            "items": [
                {**item, "_id": str(item["_id"])}
                for item in order["items"]
            ],
            "user_address": order["user_address"],
        }
        return order_dict
    return {"message": "Order not found"}

@app.put("/products/{product_id}")
def update_product(product_id: str, payload: dict):
    quantity = payload.get("quantity", 0)

    # Convert the product_id to ObjectId
    product_oid = ObjectId(product_id)

    # Check if the product exists
    existing_product = products_collection.find_one({"_id": product_oid})
    if not existing_product:
        return JSONResponse(status_code=404, content={"message": "main.py: Product not found"})

    # Update the available quantity of the product
    products_collection.update_one(
        {"_id": product_oid},
        {"$set": {"available_quantity": quantity}}
    )

    return JSONResponse(content={"message": "main.py : Product updated successfully"})
@app.get("/products/{product_id}")
def get_product(product_id: str):
    # Retrieve the product from the database based on the product_id
    product = products_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        # Return the product details as a JSON response
        product["_id"] = str(product["_id"])
        return JSONResponse(content=product)
    else:
        return JSONResponse(status_code=404, content={"message": "Product not found"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
