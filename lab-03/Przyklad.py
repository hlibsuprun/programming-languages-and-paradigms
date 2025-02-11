class Pojazd:
    def __init__(self, marka):
        self.marka = marka
    def opis(self):
        return f"Pojazd marki: {self.marka}"


class Samochod(Pojazd):
    def __init__(self, marka, model, rok):
        super().__init__(marka)
        self.model = model
        self.rok = rok

    def opis(self):
        return f"Samochod: {self.marka} {self.model} {self.rok}"

samochod1 = Samochod("toyota", "corolla", 2024) # Stworzenie obiektu
print(samochod1.opis())

# Klasa abstrakcyjna

from abc import ABC, abstractmethod

class Zwierze(ABC):
    @abstractmethod
    def dzwiek(self):
        pass

class Lew(Zwierze):
    def dzwiek(self):
        return f"Lew wydaje głos"

lew = Lew()
print(lew.dzwiek())