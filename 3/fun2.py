# funkcje zwracajace wynik

def dodaj(a,b):
    return a+b

def odejmij(a=0,b=0,c=0):
    return a-b-c #zwroc wynik do miejsca skad zostales wywolany

def oblicz_vat(cena, vat=23):
    return cena* (100+vat) / 100



print(dodaj(10,10))
print(odejmij())
print(odejmij(1))
print(odejmij(1,6))

print(odejmij(9,12)+dodaj(7,65))
print(oblicz_vat(1000))

zm = oblicz_vat(1000)
print(zm)

if zm ==1230:
    print("dziala")