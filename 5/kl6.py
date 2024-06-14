from abc import ABC, abstractmethod
class Ptak(ABC):
    """
    Klasa opisujaca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lece z szybkoscia", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass

class Kura(Ptak):
    
    def __init__(self,gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko ")

    def dziobanie(self):
        print("tu", self.gatunek, "Rozpoczynam dziobanie")

class Orzel(Ptak):

    def wydaj_odglos(self):
        print("Siueeeeee")

    def polowanie(self):
        print("tu", self.gatunek, "Rozpoczynam polowanie")

class Sowa(Ptak):
    """
    Klasa sowa
    """

    def wydaj_odglos(self):
        print("Ho HO")


# or1 = Ptak("orzel", 45)
# or1.latam()
# or1.wydaj_odglos()
#
# kur1 = Ptak("Kura domowa", 0)
# kur1.latam()
# kur1.wydaj_odglos()

kur2 = Kura("kura domowa")
kur2.latam()
kur2.wydaj_odglos()
kur2.dziobanie()

or2 = Orzel("orzel", 45)
or2.latam()
or2.polowanie()
or2.wydaj_odglos()

sowa1 = Sowa("Sowa", 25)
sowa1.wydaj_odglos()