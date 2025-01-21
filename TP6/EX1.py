def safe_division(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f"Error: {e}")


safe_division(2, 0)