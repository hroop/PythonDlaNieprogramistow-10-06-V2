class Car:
    """
    Klasa opisujaca samochod w pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizujaca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Predkosc wynosi {self.__predkosc} km/h")

    def __zmien_bieg(self):
        print("zmieniam bieg")



car = Car("tesla",2024)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# print(car.__predkosc)
car.licznik()
car.__predkosc = 0

car.licznik()
print(car.__predkosc)
car.licznik()

car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()