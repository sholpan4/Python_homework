match data:
    case [x, y]:
        print(f"List {x} and {y}")
    case (x, y, z):
        print(f"Tuple {x}, {y}, {z}")
    case _:
        print("Unknown")

