def convert_to_int(value):
    try :
        return int(value)
    except ValueError as e:
        print(f"Error: {e}")

convert_to_int("13")
