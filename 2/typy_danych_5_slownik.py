# slownik - dane typu klucz wartosc
# odpowiednik json
# klucz nie moga sie powtarzac

# pust slownik
dictionary = dict()
print(dictionary)

dictionary1 = {}
print(dictionary1)

print(type(dictionary1))
print(type(dictionary))

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

dictionary["imie"] = "Radek"
print(dictionary)
dictionary["wiek"] = 39
print(dictionary)

# nadpisanie elementu
dictionary["imie"] = "Tomek"
print(dictionary)

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

dictionary.update({"date": "12-12-2024"})
print(dictionary)

dict_small = {"x": 2}
dict_small.update([("y", 3), ("z", 4)])
print(dict_small)

print(dictionary["imie"])
# print(dictionary["name"])
print(dictionary.get("imie"))
print(dictionary.get("name", "default"))

# input() - pobiera dane np z klawiatury

# tekst = input("wpisz tekst")
# print(tekst)

dictionary2 = {}

dictionary2["kot"] = "cat"
dictionary2["pies"] = "dog"
dictionary2["slonce"] = "sun"
dictionary2["zegarek"] = "watch"
dictionary2["ksiazka"] = "book"

print(dictionary2.keys())
tekst1 = input("wpisz tekst")

print(dictionary2[tekst1])

dict_pol_and = {"kot": "cat", "pies": "dog", "jablko": "apple"}
print(dict_pol_and.keys())
odp = input("Podaj slowko")
print(dict_pol_and.get(odp.lower().replace(" ", ""), "nie mam takiego slowka"))

a = int(input("Podaj liczbe 1"))
b = input("Podaj liczbe 2")
print(a + float(b))

print(eval("3*10+15"))
