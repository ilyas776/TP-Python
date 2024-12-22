class Personne :
    def __init__(self,nom,prenom,age):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age
    
    def get_nom(self):
        return self.__nom
    
    def set_nom(self,nom):
        self.__nom=nom
    
    def get_prenom(self):
        return self.__prenom
    
    def set_prenom(self,prenom):
        self.__prenom=prenom
    @property
    def get_age(self):
        return self.__age
       
    @get_age.setter
    def age(self,age):
        self.__age=age

per1=Personne("ilyas","ily",88)
#A=per1.get_age()
#print(f"{A}")
print(per1.get_age)
#per1.set_age(20)
per1.age=20
print(per1.get_age)


    