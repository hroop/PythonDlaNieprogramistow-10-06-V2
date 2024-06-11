# kolekcja
# lista - przechwouje wiele danych roznego typu
# zachowuje kolejnosc dodawania elementow

lista = []
print(lista)
print(type(lista))

pusta_lista = list()
print(pusta_lista)

lista.append("radek")
lista.append("maciek")
lista.append("zenek")
lista.append("aldona")

print(lista)

print(lista[0])
print(lista[3])

print(len(lista))

print(lista[-1])
print(lista[-2])

# wypisac fragment

print(lista[0:3])
print(lista[:3])
print(lista[2:])
print(lista[:])
print(lista[-2:0])
print(lista[0:-2])
print(lista[2:3])
print(lista[2:10])
print(lista[7:10])
print(lista[2:2])
print(lista[0:3:2])  # start:stop:krok

lista_10 = list(range(15))
print(lista_10)
print(lista_10[-5:])

# nadpisanie elememtu
lista[2] = "mikolaj"
print(lista)

# wstawic element we wskazanie miejsce
lista.insert(1, "marek")
print(lista)
lista.insert(11, "zenek")
print(lista)

# sprawzdenie indeksu
print(lista.index("zenek"))
indeks = lista.index("zenek")
print(indeks)

# usuwanie elementu list
lista.remove("zenek")
print(lista)

lista.append("radek")
print(lista)
lista.remove("radek")
print(lista)

print("radek" in lista)  # True

#usuniecie elementu po indeksie
indeks = lista.index("mikolaj")
lista.pop(indeks)
print(lista)
print(lista.pop(0))
print(lista.pop()) #usuwa ostatni element z listy
print(lista)
lista.append("Anna")
lista.append("Tomek")
lista.append("Paulina")
print(lista)
print(lista.pop(-2))
print(lista)