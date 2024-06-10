tekst = "witaj swiecie"
print(tekst)
print(type(tekst))  # <class 'str'>

#teksty sa niemutowalne
tekst.upper()
print(tekst)  # witaj swiecie
print(tekst.upper()) #witaj swiecie
print(tekst)
tekst2 = tekst.upper()
print(tekst2) #WITAJ SWIECIE

print(tekst.lower())
tekst_lower= tekst.lower()
print(tekst.lower())

print(tekst.removesuffix("swiecie")) #witaj obcielo swiecie
print(tekst.removeprefix("witaj"))
print(" swiecie".strip()) #swiecie i usuniecie pauzy

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


