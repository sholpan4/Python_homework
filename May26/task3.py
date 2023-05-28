#task3
user_input = input("Enter square length: ")
try:
    user_int = int(user_input)
except ValueError:
    message = "Error! You have entered not number!"
else:
    result = user_int ** 2
    message = result
print(message)