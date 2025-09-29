import requests

data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

response = requests.post("http://localhost:8000/predict", json=data)

print("Status code:", response.status_code)
print("Response:", response.json())


response = requests.post("http://localhost:8000/update", json={"version": "2"})

print("Status code:", response.status_code)
print("Response:", response.json())

