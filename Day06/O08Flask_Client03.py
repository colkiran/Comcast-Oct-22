
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getplayer/ponting")
print(response.json())

print("-" * 40)
response = requests.put(BASE + 'getplayer/ponting', data={'team': 'Mumbai Indians'})
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("-" * 40)
response = requests.delete(BASE + 'getplayer/lara')

res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
