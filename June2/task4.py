#task4
def get_area(num=None, num2=None):
    # VN: теперь есть значение по умолчанию, но нет проверки на него:
    # if num2 is None

    # преобразования в int не нужны
    a = int(num)
    b = int(num2)
    if a == 0:
        return b ** 2
    elif b == 0:
        return a ** 2
    else:
        return a * b

number = get_area(0, 5) #(( для ввода только 1 аргумента все равно приходится вводить второй аргумент как "0". Это все что придумала). Правда долго не думала.
# VN: когда в функции будет проверка на None, тогда станет возможно вызывать функцию и так:
# number = get_area(5)
print(number)