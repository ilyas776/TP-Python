def process_input(user_input):
    a=int(user_input)

    return 10/a

try:
 process_input("0")
except ValueError as e:
   print(f"Error:{e}")
except ZeroDivisionError as e:
   print(f"Error:{e}")