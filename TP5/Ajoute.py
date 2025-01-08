A=input("vouler vous saisir quelque chose dans le fichier phrases : ")
try:
  with open("d:/TP_PYTHON/TP5/phrases.txt","a") as fichier :
    if A=="oui":
        fichier.write("4 phrase\n")    
except IOError:
  print("error d'ecreture")
