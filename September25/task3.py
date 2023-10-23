def get_data(data):
    match data:
        case [x, y]:
            print(f"List {x} and {y}")
        case (x, y, z):
            print(f"Tuple {x}, {y}, {z}")
        case _:
            print("Unknown")

print(get_data(("apple", "grape")))  #не реагирует на скобки круглые и прямые. Только по количеству аргументов сортирует на Лист или Тупл. нужен python 3.10 для проверки)
                                     #VN: ок, понятно. print в 10 строке выводит None