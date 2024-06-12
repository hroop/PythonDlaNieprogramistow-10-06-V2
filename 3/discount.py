from datetime import date, datetime, timedelta

today = date.today()

print("data:", today)

time = datetime.now()
print("czas", time)

tomorrow = today + timedelta(days=1)
print("Jutro", tomorrow)

print(time.time())
print(today.day)

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)

formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)

products = [
    {"sku":1, "exp_date": today, "price":100},
    {"sku":2, "exp_date": today, "price":50},
    {"sku":3, "exp_date": tomorrow, "price":250},
    {"sku":4, "exp_date": today, "price":80.0},
    {"sku":5, "exp_date": today, "price":100.0},
    {"sku":6, "exp_date": today, "price":100.0},
    {"sku":7, "exp_date": tomorrow, "price":100.0},
    {"sku":8, "exp_date": today, "price":100.0},
]

for p in products:
# print(p["sku"])
    if p["exp_date"] != today:
        continue
    p["price"] *= 0.8
    print(f"""Price for sku{p["sku"]}
is now {p["price"]}""")

