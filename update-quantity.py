import requests

product_id = "64aa8aef768eff69e87f8803"
quantity = 200

url = f"http://localhost:8000/products/{product_id}"
headers = {"Content-Type": "application/json"}
payload = {"quantity": quantity}


response = requests.put(url, headers=headers, json=payload)
if response.status_code == 200:
    print("update-quantity: Product updated successfully")
else:
    print("update-quantity: Failed to update product")
