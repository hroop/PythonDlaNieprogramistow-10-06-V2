# while - sterowana warunkiem dopoki warunek true warunek bedzie sie wkonywac

licznik = 0

while True:
    licznik += 1
    print("Komunikat 1")
    if licznik > 10:
        break

print(licznik)

licznik = 0

while licznik<10:
    licznik += 1
    print("komunikat xxx")

# password = input("Podaj haslo")
#
# # while password != "secret":
# #     password = input("Bledzne haslo. Podaj ponownie")
# #
# # print("haslo poprawne")\

lista =[]
lista_int = []

while True:
    wej = input("podaj liczbe")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)