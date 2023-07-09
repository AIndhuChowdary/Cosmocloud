# Cosmocloud
 Sample backend application in FastAPI, Python and MongoDB


# Ecommerce API

This is a sample Ecommerce API built with FastAPI and MongoDB.

## Setup

1. Install Python 3.9 or higher.
2. Clone this repository.
3. Install the required dependencies by running the following command:
**pip install 'requirement'**
4. Make sure MongoDB is installed and running locally on your machine.
5. Update the MongoDB connection URL in the `main.py` file to match your MongoDB setup.
6. Run the FastAPI application by executing the following command:
**uvicorn main:app --reload**
The API will be accessible at http://localhost:8000.

## Endpoints

- GET /products
- Retrieve a list of all products.
- GET /products/{product_id}
- Retrieve details of a specific product.
- POST /orders
- Create a new order.
- GET /orders
- Retrieve a list of all orders.
- GET /orders/{order_id}
- Retrieve details of a specific order.
- PUT /products/{product_id}
- Update the available quantity of a product.

Refer to the API documentation or explore the API endpoints using tools like cURL or Postman.

Tasks to do: 
**Create dummy dataset in mongodb**
Open MongoDB compass and in the shell:
use ecommerce              --(to create or use database)
to insert data -- 20 records: 
db.products.insertMany([
  {
    "name": "Headphones",
    "price": 50,
    "available_quantity": 15
  },
  {
    "name": "Smartwatch",
    "price": 200,
    "available_quantity": 3
  },
  {
    "name": "Camera",
    "price": 800,
    "available_quantity": 7
  },
  {
    "name": "Gaming Console",
    "price": 400,
    "available_quantity": 10
  },
  {
    "name": "Bluetooth Speaker",
    "price": 80,
    "available_quantity": 12
  },
  {
    "name": "External Hard Drive",
    "price": 120,
    "available_quantity": 6
  },
  {
    "name": "Wireless Mouse",
    "price": 30,
    "available_quantity": 20
  },
  {
    "name": "Printer",
    "price": 250,
    "available_quantity": 4
  },
  {
    "name": "Tablet",
    "price": 300,
    "available_quantity": 9
  },
  {
    "name": "Power Bank",
    "price": 40,
    "available_quantity": 18
  },
  {
    "name": "Fitness Tracker",
    "price": 100,
    "available_quantity": 5
  },
  {
    "name": "Wireless Earbuds",
    "price": 70,
    "available_quantity": 14
  },
  {
    "name": "Monitor",
    "price": 300,
    "available_quantity": 8
  },
  {
    "name": "Keyboard",
    "price": 60,
    "available_quantity": 16
  },
  {
    "name": "USB Flash Drive",
    "price": 20,
    "available_quantity": 25
  },
  {
    "name": "Smart Speaker",
    "price": 100,
    "available_quantity": 7
  },
  {
    "name": "Wireless Router",
    "price": 80,
    "available_quantity": 11
  },
  {
    "name": "Graphics Card",
    "price": 600,
    "available_quantity": 3
  },
  {
    "name": "Webcam",
    "price": 50,
    "available_quantity": 10
  },
  {
    "name": "Projector",
    "price": 500,
    "available_quantity": 5
  },
  // Add more dummy products here
])



**api to create new order:**
while the server is running (main.py) run create-order.py file in another terminal or shell 
orders collection will be created with the records mentioned in the create-order file, make sure the product_id i.e _id in the create-order file are the valid _id of products in products collection


**api to update quantity:**
while the server is running (main.py) run update-quantity.py file in another terminal or shell 
make sure the product_id is valid _id of products in products collection and provide the quantity to update
after running it produces the message and if successful it gets updated in mongodb database
but in my case after updating quantity still when I give the endpoint http://localhost:8000/products/{product_id} I'm encountering {"detail":"Method Not Allowed"} in case PUT request
but it's actually working fine in when tested in POSTMAN
so i created an additional GET method to get the updated results

**other api work with endpoints mentioned at the start**


## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create a pull request.

