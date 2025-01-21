def get_positive_integer():
    while (1):
        try:
            Nb=input("entrer un nombre positif : ")

            nb_entier=int(Nb)

            if nb_entier >0:
                return nb_entier
        except ValueError as e:
            print(f"Error:{e}")


get_positive_integer()