from abc import ABC, abstractmethod

class Vehicule(ABC):
    def deplacer(self):
        pass 

class Voiture:
    def deplacer(self):
        print("voiture")

class Bicyclette:
    def deplacer(self):
        print("Bicycmette")

Vehicule1=Vehicule()
Voiture.deplacer()
Bicyclette.deplacer()
