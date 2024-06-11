# krotka - tupla - kolekcja
# krotka jednoelementowa - zmienna niezmienna

tupla = "Radek"
print(type(tupla))

tupla_2 = "Radek"
print(type(tupla_2))

tupla_3 = "Radek"
print(type(tupla_3))

tupla_4 = ("Radek",)
print(tupla_4)
print(type(tupla_4))

tupla_names = "Radek", "Tomek", "Zenek", "Marek"
print(type(tupla_names))

tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)
print(type(tupla_liczby))

print(tupla_names.count("Tomek"))
print(tupla_names.index("Tomek"))

del tupla_liczby

tup = 1, 2
a, b = tup
x, y = 1, 2
print(a)
print(b)

# a, b = 1, 2, 3
a,*b = 1,2,3
print(a)
print(b)

print(len(tupla_names))

name1, *name2, name3 = tupla_names
print(name1, name2, name3)

*name1, name2, name3 = tupla_names
print(name1, name2, name3)

name1, name2, *name3 = tupla_names
print(name1, name2, name3)

lista = list(tupla_names)
print(lista)
print(type(lista))

print(sorted(tupla_names))

