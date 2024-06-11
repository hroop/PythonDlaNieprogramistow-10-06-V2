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

a = 1
b = 3
a = b
print("a=",a, "b=", b)
b = 7
print("a=",a, "b=", b)

lista_copy = lista.copy()
lista_2 = lista
lista.clear()
print(lista_2)
print(lista)
print(lista_copy)
print(id(lista_2))
print(id(lista))
print(id(lista_copy))

liczby = [54,999,34,12,22.34,687]
print(liczby)
# liczby = [54,999,34,12,22.34,687, "A"]
print(liczby)
print(type(liczby))

liczby.sort()
print(liczby)

# liczby = [54,999,34,12,22.34,687, "A"]
print(liczby)

lista_osob = ["radek", "ola", "agata", "lena" ]
lista_osob.sort()
print(lista_osob)

liczby.reverse()
print(liczby)

lista_osob.sort(reverse=True)
print(lista_osob)

liczby[3] = 6666
print(liczby[0:3])
print(liczby[-2])
print(liczby[-3:])

liczby.remove(54)
print(liczby)

print(liczby.pop(1))
print(liczby)
print(len(liczby)) #dlugosc listy

print(liczby[0:4:2])
print(liczby[::-1])

tekst = "Python."
lista1 = list(tekst) #rzutowanie na liste, rozpakowanie sekwencji
print(lista1)

lista3 = [tekst]
print(lista3)

krotka = tuple(liczby)
print(type(krotka))
print(krotka)

lista14 = ["radek", "radek", "radek", "radek"]

print(lista14)

lista14.insert(2, "anielka")

print((lista14))