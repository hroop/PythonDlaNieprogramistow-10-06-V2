import json

# json - {"name":"Radek"}
# obiekt typu para klucz-wartosc
# odpowiednikiem json jest w pythonie slownik

person_dict = {"name":"Radek", "age":40, "czy_pali":None}
print(type(person_dict))

with open("nasze_dane.json","w") as f:
    json.dump(person_dict, f)

with open("nasze_dane.json", "w") as f:
    json.dump(person_dict, f, indent=4)

with open("nasze_dane.json", "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

with open("nasze_dane.json", "r") as fh:
    data = json.load(fh)

print(data)
print(type(data))
print(data["name"])

#zamiana slownika na json
json_text = json.dumps(data)
print(json_text)
print(type(json_text))

#zamiana json (str)
dict_json = json.loads(json_text)
print(dict_json)
print(type(dict_json))

