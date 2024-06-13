#dziedziczenie
#przejecie cech innej klasy
#nadpisanie, modyfikowanie, rozszerzanie

class Pojazd:

    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("kolor", self.kolor)

class Samochod(Pojazd):
    """
    Klasa samochod
    """

    def __init__(self, kolor, marka=None):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()
        print(f"Marka {self.marka}")

poj = Pojazd("czerwony")
poj.info()

sam = Samochod("zielony")
sam.info()

sam2 = Samochod("Bialy", "Lambo")
lista = [poj, sam, sam2]

for i in lista:
    print(i, i.info())