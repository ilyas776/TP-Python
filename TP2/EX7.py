class livre:
    def __init__(self,titre,auteur,annee_publication):
        self.titre=titre
        self.auteur=auteur
        self.annee_publication=annee_publication
    def __str__(self):
        return f"'{self.titre}' auteur {self.auteur} en({self.annee_publication})"


class Bibliotheque:
    def __init__(self):
        self.livres=[]
    
    def ajouter_livre(self,livre):
        self.livres.append(livre)
        
    def afficher_livres(self):
        if not self.livres:
         print("La bibliothèque est vide.")
        for i in range(len(self.livres)):
         print(f"Index {i}, Book: {self.livres[i]}")

biblio1=Bibliotheque()

livre1=livre('kik','med',2000)
livre2=livre('Pio','ali',2023)

biblio1=Bibliotheque()
biblio1.ajouter_livre(livre1)
biblio1.ajouter_livre(livre2)

biblio1.afficher_livres()
          
     
