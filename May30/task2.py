user_in = input("Enter three digit number:")

try:
    num = int(user_in)
    
    num1 = num[0]
    num2 = num[1]
    num3 = num[2]
except ValueError:
    num = ""

if type(num) is int:
    if num1 == num2:
        message = "%d and %d are the same numbers " % (num1, num2)
    elif num1 == num3:
        message = "%d and %d are the same numbers " % (num1, num3)
    elif num2 == num3:
        message = "%d and %d are the same numbers " % (num2, num3)
    elif num >= 999:
        message = "Please enter three digit number!"
else:
    message = "You've entered not number!"

print(message)