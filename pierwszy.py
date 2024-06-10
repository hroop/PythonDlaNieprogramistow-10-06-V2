import sys

print()  # wypisz/wydrukuj
print("Nazywam sie Radek")
# ctrl d - powielanie elementow
print('Nazywam sie Radek')
# print('Nazywam sie Radek')
# print('Nazywam sie Radek')
# print('Nazywam sie Radek')
# ctrl / - komentowanie zaznaczonego kodu
# type() - sprawdzenie typow danych
print(type("Radek"))
print(type("39"))
print(type(39))  # int - liczby calkowite
print(type(22.33))
print(type(0.182))
print(18 - 2 * 33)
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)
print("39" + "39")  # 3939 - konkatencaja , laczenie str
# print(39+"39") jezeli sa dwa rozne typy - silne typwanie
print(int("39") + 39)  # int() rzutowanie na int (zmiana)

print(5 * "4")  # 44444

# zmienna - pudelko na dane
# snake_case
# typowanie dynamiczne - w kazdej chwili dowolny typ danych mozemy umiescic w zmiennej

name = "Radek"
print(type(name))  # str
print(name + "kowalski")  # Radekkowalski

name = 39
print(type(name))
print(str(name) + "Kowalski")
# print(name + "kowalski")

name: str = 90 # tylko podpowiedz/hint
print(name)
print(type(name)) # <class 'int'>

age = 48
print(age)
print(type(age))
print(type(age))
print(type(age))