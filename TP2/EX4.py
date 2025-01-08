class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age

    def se_presenter(self):
        print("nom:"+self.nom+"prenom :"+self.prenom+"age:"+str(self.age))

class Etudiant(Personne):
    
    def __init__(self,nom,prenom,age,matricule):
        super().__init__(nom,prenom,age)
        self.matricule=matricule
    def etud(self):
<<<<<<< HEAD
        super
        print(f"matricule:{self.matricule}")
=======
        print(f"L'étudiant {self.prenom} {self.nom} (Matricule: {self.matricule}) est en train d'étudier.")
>>>>>>> 8acc533 (First commit)

etud1=Etudiant("abdo","dodo",26,43094)
etud1.etud()

