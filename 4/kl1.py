# klasa - szablon, przepis, stempel
# obeikt - odcisk stempla
# obiekt - instancja klasy

#dfinicja klasy
class Human:
    """
    Klasa human opisujaca czlowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print("nazywam sie", self.imie)


cz1 = Human()
print(cz1)
print(cz1.imie)
cz1.imie = "ania"
cz1.wiek = 27
print(cz1.imie)
print(cz1.wiek)

cz2 = Human()
cz2.imie = "jan"
cz2.wiek = 5
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)

cz1.powitanie()
cz2.powitanie()