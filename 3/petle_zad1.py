# petle - mozliwosc wykonania wielokrotnie kodu
# for - iteracyjna

import random
from itertools import zip_longest

for i in range(5):
    print(i)

for i in range(5):
    pass

for _ in range(10):
    pass
    print(_)

for i in range(20):
    print(i * 2)

print("-------------")

lisa_kule = list(range(1, 50))

for i in range(6):
    wyn = random.choice(lisa_kule)
    print(random.choice(lisa_kule))
    lisa_kule.remove(wyn)

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

for c in lisa_kule:
    if c>10:
        print("wieksze niz 10")
    print(c)

for i in range(0,20,2):
    print(i)

for i in range(10,2,-2):
    print(i)

for i in range(-10,0):
    print(i)

lista2 = [1,2,3,1,5,6,7,2,3,5]

for c in lista2:
    if c == 3:
        c+=1
        print(c)

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
print(imiona)
print(type(imiona))

for p in imiona:
    print(p)

#wywietlic z listy elementy w postaci numer indeksu i element

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
print(imiona)
print(type(imiona))

for p in imiona:
    indeks = imiona.index(p)
    print(indeks, p)

for i in range(len(imiona)):
    print(i,imiona[i])

# enumerate (zwraca numer i element z kolekcji)

for p in enumerate(imiona):
    print(p)

a,b = (3, "Ania")
print("index",a,"element=",b)
for i,p in enumerate(imiona):
    print(i,p)

for i,p in enumerate(imiona, start=1):
    print(i,p)

ludzie = ["Radek", "Arek", "Tomek", "Ania", "Krzysztof"]
wiek = [40,34,23,30]

#wypisac w postaci imie wiek

# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])
#
# # zip - laczenie kolekcji
#
# for i in zip(ludzie, wiek):
#     print(i)

for p,w in zip(ludzie, wiek):
    print(p,w)

#wyswietlic w postaci 0 Radek 30

for i in enumerate(zip(ludzie, wiek)):
    print(i)

a, b = (0, ("Radek",40))
print(a)
print(b)
c,d = b
print(c,d)
(a, (c,d)) = (0, ("Radek", 40))
print(a,c,d)

for i ,(p,w) in enumerate(zip(ludzie, wiek)):
    print(i,p,w)

zipped = zip_longest(ludzie, wiek, fillvalue=None)
print(zipped)
#
# for zipp in zipped:
#     print(zipp)
#
# print("--------------")
#
# for i, w in zipped:
#     print(i,w)

zip_list = list(zipped)
for i in zip_list:
    print(i)

print("---------")

for i in zip_list:
    print(i,w)

#zadanie domowe - wyswietlic z indekx 0 Radek 44

