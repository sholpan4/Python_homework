# python 3.10
def get_value(value):
    match value:
        case int :
    #   case int():  , т.е. нужны скобки
            print("This is a number.")
        case str:
            print("This is a string.")
        case tuple:
            print("This is a tuple.")
        case _:
            print("Unknown type.")

print(get_value(123))
#VN: функция get_value() не возвращает ничего, поэтому тут будет напечатано None