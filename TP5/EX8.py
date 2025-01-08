try :
    with open("d:/TP_PYTHON/TP5/exemple.txt","r") as fichier :
     contenu=fichier.read() 
     print(contenu)
except FileNotFoundError:
    print("Error :fichier n'existe pas ")