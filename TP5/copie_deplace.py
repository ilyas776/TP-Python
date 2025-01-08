import shutil
#copie un ficher  
source ="d:\\TP_PYTHON\\TP5\\journal.txt"
distination="d:\\TP_PYTHON\\TP5\\copie_journal.txt"

try:
    shutil.copy(source,distination)
    print("fichier a bien copie")
except FileNotFoundError:
    print("le fichier a copie n'a pas trouver ")
except IOError:
    print("Error lors de copage de ficher")

#deplacer  un ficher
source ="d:\\TP_PYTHON\\TP5\\copie_journal.txt"
distination="d:\\TP_PYTHON\\TP5\\archives"

try:
    shutil.move(source,distination)
    print("fichier a bien deplacer")
except FileNotFoundError:
    print("le fichier a deplacer n'a pas trouver ")
except IOError:
    print("Error lors de deplacement de ficher")
