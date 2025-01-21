import logging



def log_error(message):
   # logger = logging.getLogger("E")
    logging.basicConfig(filename='d:/TP_PYTHON/TP6/Error.log', level=logging.ERROR)
    logging.error(message)
   # logger.error(message)




def read_file(filename):
    fichier= None
    try:
            fichier=  open (filename,"r")  
            lignes=fichier.readlines()
            for ligne in lignes :
                print(ligne)
    except FileNotFoundError as e :
        log_error(e)
    finally:
        print("fin de gestion de fichier")
        if fichier :
          fichier.close()

read_file("d:/TP_PYTHON/TP5/tuh.txt")