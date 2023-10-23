def get_data(data):
    match data:
        case {"name": str, "age": int}:
            print("Словарь с ключами 'name' и 'age'")
        case _:
            print("Неизвестный словарь")

print(get_data("'name': Ilon"))
#VN: ну вы поняли)))