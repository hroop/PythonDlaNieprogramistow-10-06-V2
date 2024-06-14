#REST API

# GET, POST, PUT/PARCH, DELETE
import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
print(response)

print(response.text)
response_data = response.json()
print(response_data)

for k,v in response_data.items():
    print(k, "->", v)

print(response_data["people"][0]["name"])

for p in response_data['table']:
    print(p['currency'],p['effectiveDate'],p['mid'])