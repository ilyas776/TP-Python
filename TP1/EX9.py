def analyse_texte(texte):
    mot=0
    caract=0
    new_text = texte.replace(" ", "")
    caract=len(new_text)
    mot =len(texte.split())
    return "caractére\t"+str(caract)+"\nmots\t"+str(mot)

text="je suis heureux"
print(analyse_texte(text))#carctére 13  mots 3

    