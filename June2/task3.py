#task3
def get_one_num(num, num2, num3):
    # VN: Преобразование данных - не задача этой функции
    num = str(num)
    num2 = str(num2)
    num3 = str(num3)
    result = num + num2 + num3
    return result
    # VN: функция не должна ничего печатать! Она должна вернуть число типа int
  
number = get_one_num(5, 4, 4)
print(number)
