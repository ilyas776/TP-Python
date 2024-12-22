class Produit :
    def __init__(self,prix,nom): 
        self.__prix=prix
        self.__nom=nom

    @property
    def get_nom(self):
        return self.__nom
    @get_nom.setter
    def set_nom(self,nom):
        self.__nom=nom
    @property
    def get_prix(self):
        return self.__prix
       
    @get_prix.setter
    def set_prix(self,prix):
        self.__prix=prix
    
    def calculer_prix(self,remise):
        if self.get_prix >100:
            return self.get_prix*(1-(remise/100))
        else:
            return self.get_prix
    

class Commande:
    def __init__(self,quantité,produit):
        self.quantité=quantité
        self.produit=produit
    def calculer_prix(self):
        return self.produit.calculer_prix(10)*self.quantité
    
class Panier:
    def __init__(self):
        self.Commande=[]

    def ajoute_commande(self ,commd):
         if commd not in self.Commande:
             self.Commande.append(commd)
         else:
             print("déja exesté")

    def calculer_total(self):
       total = 0
       for commande in self.Commande:
            total += commande.calculer_prix()  # Appel à la méthode `calculer_prix` de la commande
       return print(f"le prix total est{total}")
    

Produit1=Produit(260,"koca")
Produit2=Produit(33,"PARI")

A=Produit1.calculer_prix(10)
B=Produit2.calculer_prix(10)
print(f"le prix de produit 1 est : {A}")
print(f"le prix de produit 2 est : {B}")

Commande1=Commande(5,Produit1)
Commande2=Commande(20,Produit2)

panier1=Panier()
Commande1.calculer_prix()
panier1.ajoute_commande(Commande1)
panier1.ajoute_commande(Commande2)
panier1.ajoute_commande(Commande1)
panier1.calculer_total()





