file_name=input("entrer le nom de file")
Nb=input("entere un nombre:")
try:
    conv_nb=int(Nb)
    fichier=  open (file_name,"r")  
    lignes=fichier.readlines()
    for ligne in lignes :
         print(ligne)
except FileNotFoundError as e:
     print(f"Error:{e}")
except IOError as e:
     print(f"Error:{e}")
except FileExistsError as e:
     print(f"Error:{e}")
except ValueError as e:
     print(f"Error:{e}")