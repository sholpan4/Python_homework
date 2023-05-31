#task6
print("a * x + b = 0")
user_inputa = input("Enter a = ")
user_inputb = input("Enter b = ")

try:
    num_a = int(user_inputa)
    num_b = int(user_inputb)
except ValueError:
    message = "Error! You have entered not number!"
else:
    result = (-num_b)/num_a   # VN: эту строку тоже можно поместить в блок try и перехватить ZeroDivisionError
    message = print('x =', result)

print(message)