class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age <0:
        raise NegativeAgeError("l'age est infirieure de 0 ")
    else:
        return age
    
try:
 set_age(-6)
except NegativeAgeError as e:
   print(f"Error:{e}")