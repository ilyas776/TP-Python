import csv
with open("d:\\TP_PYTHON\\TP5\\contacts.csv",mode="r",newline='') as fichier :
    lecture=csv.reader(fichier)
    next(lecture, None)  # Ignorer les en-têtes
    for ligne in lecture:
        print(f"Nom : {ligne[0]}, Âge : {ligne[1]}, Ville : {ligne[2]}") 
