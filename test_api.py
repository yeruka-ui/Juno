import requests

res = requests.post("http://127.0.0.1:5000/ask", json={"message": "Hello Nemotron!"})

# Debug output
print("Status code:", res.status_code)
print("Raw response:", res.text)

try:
    print("JSON response:", res.json())
except Exception as e:
    print("Failed to decode JSON:", e)

