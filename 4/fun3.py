a = 10
b = 10




def dodaj():
    a = 6  # zmienne o zasiegu lokalnym tylko w tej funkcji
    b = 7
    print(a)

def dodaj2():
    print(a+b)

def dodaj3():
    global a
    a = 8
    b = 9
    print(a+b)

def zwraca_wiele():
    return 1,2,3

dodaj2()
print("Wartosc a z gory (globalne)",a)
dodaj()
print("Wartosc a z gory (globalne)",a)
dodaj3()
print("Wartosc a z gory (globalne)",a)
dodaj2()
print("Wartosc a z gory (globalne)",a)
print(zwraca_wiele())
