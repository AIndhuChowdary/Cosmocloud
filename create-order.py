import requests

url = "http://localhost:8000/orders"

order_data = {
    "timestamp": "2023-07-09T12:00:00Z",
    "items": [
        {
            "_id": "64aa8aef768eff69e87f8807",  # Replace with the correct product id
            "bought_quantity": 2,
            "total_amount": 500.0
        },
        {
            "_id": "64aa8aef768eff69e87f8811",  # Replace with the correct product id
            "bought_quantity": 2,
            "total_amount": 1200.0
        }
    ],
    "user_address": {
        "city": "Bangalore",
        "country": "India",
        "zip_code": "517002"
    }
}

response = requests.post(url, json=order_data)

if response.status_code == 200:
    print("Order created successfully")
else:
    try:
        error_response = response.json()
        print("Failed to create order:", error_response)
    except ValueError:
        print("Failed to create order. Invalid response:", response.text)
