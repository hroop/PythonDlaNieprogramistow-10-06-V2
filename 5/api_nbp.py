import requests as re

url = "http://api.nbp.pl/api/exchangerates/rates/A/EUR/"

response = re.get(url)
print(response.text)

response_data = response.json()
currency = response_data["currency"]
print("waluta", currency)
effective_date = response_data["rates"][0]["effectiveDate"]
mid = response_data["rates"][0]["mid"]
print(f"Waluta {currency}, data: {effective_date} kurs: {mid}")