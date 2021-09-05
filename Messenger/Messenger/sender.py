import requests


r = requests.post(
    "http://127.0.0.1:5000/send",
    json={"text": "Year, let's do it", "name": "Patrick"}
)

print(r)
print(r.headers)
print(r.text)