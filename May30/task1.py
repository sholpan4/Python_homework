#task1
user_in = input("Enter any one digit number from 0 to 9:")

try:
    num = int(user_in)
except ValueError:
    num = ""

if type(num) is int:
    if num == 0:
        message = "Special symbol for 0 on the keyboard = )"
    elif num == 1:
        message = "Special symbol for 1 on the keyboard = !"
    elif num == 2:
        message = "Special symbol for 2 on the keyboard = @"
    elif num == 3:
        message = "Special symbol for 3 on the keyboard = #"
    elif num == 4:
        message = "Special symbol for 4 on the keyboard = $"
    elif num == 5:
        message = "Special symbol for 5 on the keyboard = %"
    elif num == 6:
        message = "Special symbol for 6 on the keyboard = ^"
    elif num == 7:
        message = "Special symbol for 7 on the keyboard = &"
    elif num == 8:
        message = "Special symbol for 8 on the keyboard = *"
    elif num == 9:
        message = "Special symbol for 9 on the keyboard = ("
    elif num > 9:
        message = "Please enter one digit number!"
else:
    message = "You've entered not number!"

print(message)