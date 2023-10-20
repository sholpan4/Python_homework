def get_point(point):
    
    match point:
        case (x, y) if x > 0 and y > 0:
            print(f"Точка в первом квадранте: x={x}, y={y}")
        case (x, y) if x < 0 and y > 0:
            print(f"Точка во втором квадранте: x={x}, y={y}")
        case _:
            print("Точка не в первом и не втором квадранте")

print(get_point(3, 7))