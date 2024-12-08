class voiture:
    marque=''
    modèle=''
    année=0

    def afficher_info(self):
        print ("la marque de la voiture est:"+ self.marque +" son module est:"+ self.modèle +" année "+ str(self.année))


voiture1=voiture()
voiture1.année=2000
voiture1.marque="Skoda"
voiture1.modèle="pipo"
voiture1.afficher_info()
voiture2=voiture()
voiture2.année=2010
voiture2.marque="dacia"
voiture2.modèle="duster"
voiture2.afficher_info()



