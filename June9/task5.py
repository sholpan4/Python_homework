#task5
num = int(input("Enter six digit number:"))
n = int(input("How many digits to replace?"))
result = 0

while n > 0:   
    last_digit = num % 10
    num = num // 10
    result = last_digit * 100000 + num
    n -= 1
else:
    result

print(result)
#(( не смогла переставить полностью, подсказку пожалуйста