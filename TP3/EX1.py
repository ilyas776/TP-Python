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
    return (self.rayon**2)*math.pi
  
class Rectangle:
  def __init__(self,largeur,langeur):
        self.largeur=largeur
        self.langeur=langeur
       
  def calculer_surface(self):
    return self.langeur*self.largeur

Cercle1=Cercle(26)
Rectangle1=Rectangle(12,26)

A=Cercle1.calculer_surface()
B=Rectangle1.calculer_surface()
print(f"la surface de cercle {A}")
print(f"la surface de rectangle {B}")


   