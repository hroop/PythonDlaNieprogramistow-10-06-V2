user = "tomek"
wiek = 39
wersja = 3.9000001
print(type(wersja))
liczba = 123454534562362
print(type(liczba))

print("witaj %s masz teraz %d lat" % (user, wiek))

print("witaj %(user)s, masz teraz %(wiek)d lat." % {"user": user, "wiek": wiek})
print("witaj %(user)s, masz teraz %(age)d lat." % {"user": user, "age": wiek})

print(f"witaj {user}, masz teraz {wiek} lat.")

print("uzywamy wersji Pythona %i" % 3)
print("uzywamy wersji Pythona %f" % 3.222)
print("uzywamy wersji Pythona %.2f" % 3.222)
print("uzywamy wersji Pythona %.0f" % 3.222)
x= 3.14
print("zero miejc po przecinku %.f" % x)
print("x sie nie zmienilo", x)

y = round(x)
print("y=", y)

x=3.1415
print(round(x,2))

print(f"uzywamy wersji python {wersja}")
print(f"uzywamy wersji python {wersja:.1f}")
print(f"uzywamy wersji python {wersja:.2f}")

print(f"{user:>10}")
print(f"{user:<20}")
print(f"{user:^20}")

print(liczba)
print("nasza duza liczba {:,}".format(liczba))
print("nasza duza liczba {:,}".format(liczba).replace(",","."))
print("nasza duza liczba {:,}".format(liczba).replace(","," "))

print(f"nasza duza liczba {liczba:,}")
print(f"nasza duza liczba {liczba:,}".replace(".", ","))
print(f"nasza duza liczba {liczba:,}".replace(".", ","))

liczba_2 = 123_456_789_123
print(liczba_2)

print(f"nasza duza liczba {liczba_2:,}".replace(","," "))
