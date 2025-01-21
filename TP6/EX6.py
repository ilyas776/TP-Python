def safe_division(a, b):
        return a/b
    

try:
    safe_division(2, 3)
except ZeroDivisionError as e:
        print(f"Error: {e}")
else:
        print("division effectuer avec succés")
finally:
        print("la fonction est terminer")

