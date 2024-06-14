# pracownik - imie, nazwisko, pensja
# manager - imie, nazwisko, pensja, premia
# konstruktor
# metode przedstaw sie
# metode oblicz pensje

class Pracownik:
    lista = []
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def powitanie(self):
        print("nazywam sie", self.imie, self.nazwisko)
        zmienna1 = (self.imie, self.nazwisko)

        self.lista.append(zmienna1)
        print(self.lista)


    def oblicz_pensje(self):
        print(f"Pensja  {self.pensja}")

class Manager(Pracownik):
    """
    Klasa manager
    """

    def __init__(self, imie, nazwisko, pensja, premia=None):
        super().__init__(imie, nazwisko, pensja)

        self.premia = premia

    def oblicz_pensje(self):
        print(f"Pensja  {self.pensja + self.premia}")

cz1 = Pracownik("ania", "j", 1000)
cz1.powitanie()
cz1.oblicz_pensje()

cz2 = Manager("jan", "k", 2000, 500)
cz2.powitanie()
cz2.oblicz_pensje()

cz3 = Pracownik(input("jakie imie"), input("jakie naziwsko"), 1000)
cz3.powitanie()
cz3.oblicz_pensje()
print(Pracownik.lista)


