# zbiór, set - przechwouje unikalne elementy
# nie zachowuje kolejnosci przy dodawaniu elementow
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(type(zbior))
print(zbior)

zb2 = set()  # utworzenie pustego zbioru
print(zb2)  # set()

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)

# pop() - usuniecie pierwszego elementu zabiotu

print(zbior.pop())

# usuniecie po elemencie
zbior.remove(55)
print(zbior)

zbior_copy = zbior.copy()
print(zbior_copy)

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.24}
print(zbior_2)

# suma zbiorow
print(zbior | zbior_2)
print(zbior)
print(zbior_2)

zbior.add(0)
print(zbior.union(zbior_2))

#czesc wspolna
print(zbior & zbior_2)
print(zbior.intersection(zbior_2))
print(zbior-zbior_2)
print(zbior.difference(zbior_2))
print(zbior_2.difference(zbior))

#laczy zbiory - zmiana bazowy
zbior.update(zbior_2)
print(zbior_2)

#roznica symetryczna
print(zbior_2)
zbior_3 = {66,777,11,44,18,22}
print(zbior_3)
print(zbior_3 ^ zbior_2)
print(zbior_3.symmetric_difference(zbior_2))

lista = list(zbior_3)
print(lista)

krotka = tuple(zbior_3)
print(krotka)