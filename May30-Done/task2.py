#task2
user_in = input("Enter three digit number:")

try:
    num = str(user_in) #можно не писать str 150623
    
    num1 = num[0]
    num2 = num[1]
    num3 = num[2]
except ValueError:
    num = ""

if num1 == num2 == num3:
    message = "All three digit numbers: %s, %s, %s are the same" % (num1, num2, num3)
elif num1 == num2:
    message = "%s and %s are the same numbers " % (num1, num2)
elif num1 == num3:
    message = "%s and %s are the same numbers " % (num1, num3)
elif num2 == num3:
    message = "%s and %s are the same numbers " % (num2, num3)
else:
    message = "All three numbers are not same."

print(message)