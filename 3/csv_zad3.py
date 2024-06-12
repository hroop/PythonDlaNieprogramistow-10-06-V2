import pandas

data = pandas.read_csv("nasze_dane2.csv", delimiter=";")
print(data)

print(data.columns)
print(data.values)
print(data.items)