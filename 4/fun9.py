# funkcja lambda - skrocony zapis funkcji
# zwraca wynik
# fynkcja anonimowa

def odejmin2(a, b):
    return a - b


print(odejmin2(8, 4))

odejmij = lambda a, b: a - b
print(odejmij(5, 2))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000, 8))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosly")
print(wiek(11))

lista = [1, 2, 5, 34, 56, 100, 200, 500]

lista_wynik = []
for i in lista:
    lista_wynik.append(i * 2)

print(lista_wynik)
print([i * 2 for i in lista])

def zmien(x):
    return x * 2

lista_wynik_funkcja = []

for i in lista:
    lista_wynik_funkcja.append(zmien(i))
print(lista_wynik_funkcja)

#funkcja wyzszego rzedu
# map() - pobiera element z kolecji, wykonuje na nim zadana funkcje

print(f"zastosowanie map {list(map(zmien, lista))}")
print(f"zastosowanie map {list(map(lambda x: x*2, lista))}")
print(f"zastosowanie map {list(map(lambda x: x*4, lista))}")

#filtrowanie danych

l3 = []
for i in lista:
    if i<3:
        l3.append(i)
print(l3)

# filter pobiera dane zwraca spelniajace warunek

print(f"zastosowane filter(): {list(filter(lambda x: x < 3, lista))}")
print(f"zastosowane filter(): {list(filter(lambda x: x < 300, lista))}")
print(f"zastosowane filter(): {list(filter(lambda x: x > 3 and x < 150, lista))}")