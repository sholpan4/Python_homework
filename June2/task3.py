#task3
def turn_one_num(num, num2, num3):
    # VN: Преобразование данных - не задача этой функции
    num = int(num)
    num2 = int(num2)
    num3 = int(num3)
    message = ("%d%d%d" % (num, num2, num3))
    print(message)
    # VN: функция не должна ничего печатать! Она должна вернуть число типа int
  
number = turn_one_num(5, 4, 4)
