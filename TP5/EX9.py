try :
     with open("d:/TP_PYTHON/TP5/exemple.txt","r") as fichier :
        contenu=fichier.readlines() 
        total_lignes = len(contenu)
        total_mots = sum(len(ligne.split()) for ligne in contenu)
        total_caracteres = sum(len(ligne) for ligne in contenu)
        print(f"le nombre de lignes est :{total_lignes}")
        print(f"le nombre de mots est :{total_mots}")
        print(f"le nombre de caractéres est :{total_caracteres}")
except IOError:
    print("Error:")