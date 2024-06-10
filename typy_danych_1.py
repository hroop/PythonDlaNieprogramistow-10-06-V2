import sys

wiek = 47
rok = 2024
temp = 36.6
temp_2 = 36, 6

print(type(temp_2))

print(temp)
print(type(temp))

print(5 * wiek)
print(5 * "wiek")

print(wiek * rok)
print(wiek + rok)
print(wiek - rok)
print(wiek / rok)
print(rok // wiek)

print(rok % wiek)  # modulo
print(5 % 2)
print(wiek ** rok)
print(len(str(wiek ** rok)))
# print(len(str(wiek ** rok **2)))

print(54 - 5 * 43 + 4 / 2 + 4 / 2)
print(54 - 5 * 43 + (4 / 2 + 4) / 2)

print(0.2 + 0.8)
print(0.2 + 0.7)
print(0.1 + 0.2)

print(sys.float_info)

print(f"sprawdzenie zmiennej {temp} {wiek}")
print(f"""{temp} 
{wiek}""")

# typ logiczny prawda lub falsz
# True, False

czy_znasz_python = True
print(czy_znasz_python)
print(type(czy_znasz_python))
# 1 - prawda, 0 - fałsz

print(int(False))
print(int(czy_znasz_python))

x = 1
print(bool(x))
x = 100
print(bool(x))

x = -102
print(bool(x))
x = 0.1
print(bool(x))
x = "radek"
print(bool(x))
x = ""
print(bool(x))
x = None
print(bool(x))

# dzialania logicznie

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(False or True)
print(True or False)
print(False or False)

print(not True)
print(not False)

x = 0
print(not x == 1)

a=8
b=6
print(f"Porownanie {a} > {b}", a>b)
print(f"Porownanie {a} < {b}", a<b)
print(f"Porownanie {a} == {b}", a==b)
print(f"Porownanie {a} != {b}", a!=b)
print(f"Porownanie {a} >= {b}", a>=b)
print(f"Porownanie {a} <= {b}", a<=b)