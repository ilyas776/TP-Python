class Employe :
    def __init__(self,nom,prénom,salaire): 
        self.prénom=prénom
        self.nom=nom
        self.salaire=salaire
    def affiche(self):
        print(f"le nom : {self.nom} ,{self.prénom} , {self.salaire}")
class Manager(Employe):
    def __init__(self,nom,prénom,salaire): 
        super().__init__(nom,prénom,salaire)
        self.Employe=[]

    def ajoute_emploi(self ,emplo):
         if emplo not in self.Employe:
             self.Employe.append(emplo)
         else:
             print("déja exesté")

    def affiche_liste(self,emplo):
        if emplo not in self.Employe:
            print("n'existe pas!!!!!")
        else:
            print("Liste des employés :")
            for employe in self.Employe:
                employe.affiche()

emplo1=Employe("tako","koca",12)
emplo2=Employe("papap","ilyas",12)
emplo3=Employe("kali","ali",12)

Manager1=Manager("kali","ali",12)
Manager1.ajoute_emploi(emplo1)
Manager1.ajoute_emploi(emplo2)
Manager1.affiche_liste(emplo2)