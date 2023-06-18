#task4
user_input  =input("Enter kilometer: ")
try:
    user_int = int(user_input)
#1km=0.621371mile
except ValueError:
    message = "Error! You have entered not number!"
else:
    result = user_int * 0.621371
    message = result
print(message)