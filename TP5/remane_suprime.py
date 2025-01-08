import os
#renomer un ficher  
ancien_name="d:\\TP_PYTHON\\TP5\\phrases1.txt"
nouveau_name="d:\\TP_PYTHON\\TP5\\anciennes_phrases.txt"

try:
    os.rename(ancien_name,nouveau_name)
    print("fichier a bien renomer")
except FileNotFoundError:
    print("le fichier a renomer n'a pas trouver ")
except IOError:
    print("Error lors de renomage de ficher")

#suprimer un ficher

try:
    os.remove(nouveau_name)
    print("fichier a bien suprimer")
except FileNotFoundError:
    print("le fichier a suprimer n'a pas trouver ")
except IOError:
    print("Error lors de suprission de ficher")
