#task5
num = int(input("Enter six digit number:"))
n = int(input("How many digits to replace?"))
result = 0

while n > 0:   
    last_digit = num % 10
    num = num // 10
    result = last_digit * 100000 + num
    n -= 1
else:  # VN: этот else тут ни к чему
    result

print(result)
#(( не смогла переставить полностью, подсказку пожалуйста

# VN: Перед тем как применить подсказку, пройдите внимательно отладчиком по всей программе и посмотрите,
# как и на каких шагах меняются переменные
# Подсказка: уберите переменную result, а вместо неё используйте num
# Снова пройдите программу по шагам с помощью отладчика
