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

#wypisac fragment

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
print(lista[0:3:2]) #start:stop:krok