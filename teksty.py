tekst = "witaj swiecie"
print(tekst)
print(type(tekst))  # <class 'str'>

# teksty sa niemutowalne
tekst.upper()
print(tekst)  # witaj swiecie
print(tekst.upper())  # witaj swiecie
print(tekst)
tekst2 = tekst.upper()
print(tekst2)  # WITAJ SWIECIE

print(tekst.lower())
tekst_lower = tekst.lower()
print(tekst.lower())

print(tekst.removesuffix("swiecie"))  # witaj obcielo swiecie
print(tekst.removeprefix("witaj"))
print(" swiecie".strip())  # swiecie i usuniecie pauzy

print(tekst)

print(tekst.count("i"))
print(tekst.count("i", 0, 4))

print(tekst.count("i", 5, 9))
print(tekst.count("j", 0, 4))
print(tekst[3])

encoded_s = tekst.encode("utf-8")
print(encoded_s)
print(type(encoded_s))
print(encoded_s.decode("utf-8"))

imie = "Radek"
tekst_format = f"Mam na imie {imie}i lubie Pythona"
# 3 f - f string - tekst sformatowany
# w {} wpisujemy zawartsc zmiennej
print(tekst_format)
tekst_format_2 = f"\tMam na imie {imie}\ni lubie Pythona\b"
print(tekst_format_2)

starszy = "witaj %s!"  # oczkuje stringa
print(starszy % imie)

print("witaj {}!".format(imie))

#tekst wielolinijakowy
print("""Tekst
Wielolinijkowy
sformatowany""")

# Tekst
# Wielolinijkowy
# sformatowany
