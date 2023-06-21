import requests

api_url = "http://127.0.0.1:5000"
response = requests.get(api_url)
print(response.json())
