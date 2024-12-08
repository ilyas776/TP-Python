class Rectangle:
   largeur =0
   hauteur =0
   def __init__(self,largeur,hauteur):
      self.hauteur=hauteur
      self.largeur=largeur
   def calculer_surface(self):
      resultat=self.largeur*self.hauteur
      return resultat

   def calculer_perimetr(self):
      resultat=(self.largeur+self.hauteur)*2
      return resultat
   
rectangle1=Rectangle(12,9)
print("Perimeter:", rectangle1.calculer_perimetr())
print("Surface area:", rectangle1.calculer_surface())