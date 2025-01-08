try:
  with open("d:/TP_PYTHON/TP5/phrases.txt","w") as fichier :
    fichier.write("1 phrase\n")    
    fichier.write("2 phrase\n")    
    fichier.write("3 phrase\n")
except IOError:
  print("error d'ecreture")
