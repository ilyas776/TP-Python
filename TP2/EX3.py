class banque:
    titulaire="" 
    solde=0
    def __init__(self,titulaire,sold):
        self.solde=sold
        self.titulaire=titulaire

    def deposer(self,montant):
        self.solde+=montant
        return self.solde
    
    def retirer(self,montant):
        self.solde-=montant
        return self.solde
    
    def afficher_solde(self):
        print("le sold est:"+ str(self.solde))
    

banque1=banque("kd",2000)
banque1.deposer(200)
banque1.retirer(100)
banque1.afficher_solde()
 
 
    
