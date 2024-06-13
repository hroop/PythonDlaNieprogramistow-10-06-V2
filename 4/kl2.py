class Human:
    """
    Klasa human definiujaca czlowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizujaca (konstruktora)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec
    def powitanie(self):
        print("nazywam sie", self.imie)

    def wzrost1(self):
        print("moj wzrost", self.wzrost)

    def wiek1(self):
        print("tyle mam lat", self.wiek)

    def plec1(self):
        print("moja plec to", self.plec)

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszylem w droge")
        else:
            print("Ruszylam w droge")



cz1 = Human("ania", 27, 165)
print(cz1.plec)
print(cz1.wiek)
print(cz1.wzrost)
cz1.powitanie()
cz1.wiek1()
cz1.wzrost1()
cz1.plec1()

cz2 = Human("Radek", 45, 190,"m")
cz2.wzrost1()

lista =[cz1,cz2]
for i in lista:
    i.powitanie()
    i.ruszaj()