from abc import ABC,abstractmethod
import math
class Form(ABC):
  @abstractmethod
  def calculer_surface():
    pass

class Cercle:
  def __init__(self,rayon):
        self.rayon=rayon
       
  def calculer_surface(self):
    return (f"Cercle {(self.rayon**2)*math.pi}")
  
class Rectangle:
  def __init__(self,largeur,langeur):
        self.largeur=largeur
        self.langeur=langeur
       
  def calculer_surface(self):
    return (f"Rectangle {self.langeur*self.largeur}")

def afficher_surface(Forms):
   for form in Forms:
      print(f"la surface du {form.calculer_surface()} ")




frome =[
      Rectangle(12,45),
      Cercle(24)
]
afficher_surface(frome)

