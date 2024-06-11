# #wyjatki = rzucanie obsluga
#
#  print(5/0)


try:
    # print(5/0)
    # print(5/"00")
# print("A"+9)
    print(int("A"))
    wynik = 5/1

except ZeroDivisionError:
    print("dzielenie przez zero")
except TypeError:
    print("rozne typy danych")
except ValueError:
    print("blad wartosci")
except Exception as e:
    print("wystawpil blad", e)
else:
    print("wynik", wynik)
finally:
    print("skonczylem")

print("program napotkal blad")

