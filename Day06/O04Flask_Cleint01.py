
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld")

print(response)
print(response.json())

for k, v in response.json().items():
    print(k,  "=>",  v)

