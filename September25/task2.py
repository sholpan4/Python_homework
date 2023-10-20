# python 3.10
match value:
    case int :
        print("This is a number.")
    case str:
        print("This is a string.")
    case tuple:
        print("This is a tuple.")
    case _:
        print("Unknown type.")

