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
    
Produit1=Produit(260,"koca")

A=Produit1.calculer_prix(10)

print(f"le prix est : {A}")
