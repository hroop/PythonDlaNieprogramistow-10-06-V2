dictionary = {"imie":"Radek", "naziwsko": "kowalski"}

#wyswietli klucze
for k in dictionary:
    print(k)

#wartosci
for v in dictionary.values():
    print(v)

#pary
for i in dictionary.items():
    print(i)

for k,v in dictionary.items():
    print(k, "=>", v)

for k,v in dictionary.items():
    print(k,v,sep="=>")

print("Radek", end="")
print("Tomek")
print("Nastepny wiersz")

dictionary2 = {"imie":"Radek", "naziwsko": "kowalski"}
d={}

for k,v in dictionary2.items():
    d[v] = k
    print(dictionary2)
    print(d)
    print({value:key for key, value in dictionary2.items()})