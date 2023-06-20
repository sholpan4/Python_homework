#task4
num = int(input("Enter number:"))

even = 0
odd = 0
# negetive = 0
possitive = 0
zero = 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10  # VN: эта строка не нужна. Непонятно для чего это деление
                     # UPD: кажется, понял вашу мысль, но 10 раз повторить цикл - это делается по-другому

    # if num < 0:
    #     negetive += 1
    if num > 0:
        possitive +=1
    elif num == 0:
        zero +=1

print(f'Even: {even}, odd: {odd}')
print(f'Possitive: {possitive}, zero: {zero}') #negetive: {negetive}

#((( не могу понять как вводить отрицательные числа (посчитать условия вроде правильные)
# VN: строку 2 перенесите внутрь цикла. А цикл должен быть другой, чтобы повторялся только 10 раз