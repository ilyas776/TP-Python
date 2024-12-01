def compte_occurences(liste1):
    mots={}
    for i in liste1:
        if i in mots:
           mots[i]+=1
        else:
           mots[i]=1
    return mots
   

liste1=["ba","pa","pa","ba"]

print(compte_occurences(liste1))#{ba:2 ; pa:2}



