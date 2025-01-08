import csv

def add_contact(file_name):
    name = input("Entrez le nom: ")
    age = input("Entrez l'Age': ")
    ville = input("Entrez la ville : ")

    with open(file_name, mode='a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, ville])
        print(" ajouté avec succès.")

def afficher_contact(file_name):
    """
    affiche contact .
    """
    try :
     with open(file_name,"r") as fichier :
      contenu=csv.reader(fichier)
       # Ignorer la première ligne (en-têtes)
      next(contenu, None)
      for ligne in contenu:
        print(f"Nom : {ligne[0]}, Âge : {ligne[1]}, Ville : {ligne[2]}") 
    except FileNotFoundError:
     print("Error :fichier n'existe pas ")

def cherche_contact(file_name):
    """
    Adds a contact .
    """
    nom_recherche = input("Entrez le nom à rechercher : ")
    try:
      with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        contacts = list(reader)

        resultats = [contact for contact in contacts[1:] if contact[0].lower() == nom_recherche.lower()]

        if resultats:
            print(f"\nContacts trouvés pour le nom '{nom_recherche}' :")
            for contacts in resultats:
                print(f" {resultats}")
        else:
            print(f"Aucun contact trouvé pour le nom '{nom_recherche}'.")
    except FileNotFoundError:
     print("Error :fichier n'existe pas ")

def suprimer_contact(file_name):
    name_to_delete = input("Entrez le nom du contact à supprimer: ")

    try:
        # Lire tous les contacts
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            contacts = list(reader)

        # Filtrer les contacts qui ne correspondent pas au nom
        new_contacts = [contact for contact in contacts if contact[0].lower() != name_to_delete.lower()]

        if len(new_contacts) == len(contacts):
            print("Aucun contact trouvé avec ce nom.")
        else:
            # Réécrire le fichier avec les contacts restants
            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_contacts)
            print(f"Le contact '{name_to_delete}' a été supprimé avec succès.")
    
    except FileNotFoundError:
        print("Aucun contact trouvé. Le fichier n'existe pas encore.")


def main(name_file):
   while True:
        print("\n1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact par nom")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choice = input("Choisissez une option (1/2/3/4/5): ")

        if choice == '1':
            add_contact(name_file)
        elif choice == '2':
            afficher_contact(name_file)
        elif choice == '3':
            cherche_contact(name_file)
        elif choice == '4':
            suprimer_contact(name_file)
        elif choice == '5':
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

main("D:\TP_PYTHON\TP5\contacts.csv")
