#task2
user_input1 = input("Enter number: ")
user_input2 = input("Enter number: ")

try:
    user_int1 = int(user_input1)
    user_int2 = int(user_input2)
except ValueError:
    message = "Error! You have entered not number!"
else:
    result = (user_int1+user_int2) // 2
    message = result
print(message)
