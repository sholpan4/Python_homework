match value:
    case 0 | 1:
        print("Ноль или один")
    case 2 | 3 | 4:
        print("Два, три или четыре")
    case _:
        print("Другое число")
