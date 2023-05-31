name = "Sholpan"
print(name)

#task1
user_input = input("Enter number: ")

try:
    user_int = int(user_input)
except ValueError:
    message = "Error! You have entered not number!"
else:
    result = user_int ** 2
    message = result
print(message)