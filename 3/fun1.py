# funkcje - wydzielony fragment programu do wykonania w dowolnym momencie. Mozna go wkonac wielokrotnie
# deklaracja funkcji musi nastapic wczesniej niz jej wywolanie
# w miejscu deklaracji funkcja nic nie wykonuje

a = 8
b = 9


# deklaracja funkcji
def dodaj(): #funkja bezaruemtnowa
    print(a + b)

def dodaj2(a,b):
    print(a+b)

def odejmij(a,b,c=0): #ab obowiazkowe, c domyslny
    print(a-b-c)


# uzycie funkcji
dodaj()
dodaj2(7,56)
odejmij(1,2) #argumenty pozycyjne
odejmij(b=9,c=1,a=3) #argumenty po nazwie

