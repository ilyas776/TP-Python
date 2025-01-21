def read_file(filename):
    fichier= None
    try:
            fichier=  open (filename,"r")  
            lignes=fichier.readlines()
            for ligne in lignes :
                print(ligne)
    except FileNotFoundError as e :
        print(f"Error : {e}")
    finally:
        print("fin de gestion de fichier")
        if fichier :
          fichier.close()

read_file("d:/TP_PYTHON/TP5/tuh.txt")