class Vehicule:
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee
    def afficher_info(self):
        print(f"la marque{self.marque},le module {self.modele},annee {self.annee}")

    
class Moteur:
    def __init__(self,puissance,type_moteur):
        self.puissance=puissance
        self.type_moteur=type_moteur
    def afficher_moteur(self):
        print(f"la puissance{self.puissance},le type {self.type_moteur}")

class voiture(Vehicule,Moteur):
    def __init__(self, marque, modele, annee,puissance,type_moteur,nombre_de_places):
        Vehicule.__init__(self,marque, modele, annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.nombre_de_places=nombre_de_places

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print(f"Nombre de places {self.nombre_de_places}")

class Moto(Vehicule,Moteur):
    def __init__(self, marque, modele, annee,puissance,type_moteur,type_moto):
        Vehicule.__init__(self,marque, modele, annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.type_moto=type_moto

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print(f"type de moto  {self.type_moto}")

voiture1=voiture("fiat","500", 2022,100,"BJ",5)    
moto1=Moto("HUNDAY","TITO", 2023,120,"KLL","Sport")
print("========>information de voiture")
voiture1.afficher_info()
print("=========>information de moteur")
moto1.afficher_info()