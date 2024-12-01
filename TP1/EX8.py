def somme_varrags(*args):
    som=0
    for num in args:
        som+=num
    return som

print(somme_varrags(1,3,4))#8
