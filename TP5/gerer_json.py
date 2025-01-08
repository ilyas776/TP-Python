import json
with open("d:\\TP_PYTHON\\TP5\\etudiants.json", "r") as fichier:
       data = json.load(fichier)

# Vérifier le contenu global
print(data)

# Afficher les informations de chaque étudiant
for etudiant in data["Etudiant"]:
    print(f"Nom : {etudiant['Nom']}, Âge : {etudiant['Age']}, Note : {etudiant['Note']}")