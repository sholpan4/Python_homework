# python 3.10
def get_value(value):
    match value:
        case int :
            print("This is a number.")
        case str:
            print("This is a string.")
        case tuple:
            print("This is a tuple.")
        case _:
            print("Unknown type.")

print(get_value(123))