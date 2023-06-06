def get_num(num, num2):
    if num < num2:
        template = -1
        message = template
    elif num > num2:
        template = 1
        message = template
    elif num == num2:
        template = 0
        message = template
    else:
        message = "Please enter number!"
    print("Result is:", message)

num = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

result = get_num
print("Result is:", result)