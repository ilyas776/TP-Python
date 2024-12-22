class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.ami=[]

    def se_presenter(self):
        print("nom:"+self.nom+"prenom :"+self.prenom+"age:"+str(self.age))

    def ajouter_ami(self,ami):
        if ami not in self.ami:
            self.ami.append(ami)
        else :
         print(f"deja ajouter {ami.nom}")

    def afficher_amis(self):
        if not self.ami:
         print("aucun ami.")
        for amis in self.ami:
            print(f"- {amis.prenom} {amis.nom}")

par1=Personne("abdo","dodo",26)
par2=Personne("ilyas","bibo",26)
par3=Personne("med","tajo",26)

par1.ajouter_ami(par3)
par1.ajouter_ami(par2)
par1.ajouter_ami(par2)

par1.afficher_amis()