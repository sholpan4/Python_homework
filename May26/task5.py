#task5 
user_in1 = input("Enter first number: ")
user_in2 = input("Enter second number: ")

template = """
Addition:       %.2f
Subtraction:    %.2f
Multiplication: %.2f
Division:       %.2f
""" 
try:
    num1 = float(user_in1) 
    num2 = float(user_in2)
except ValueError:
    message = "Error! You have entered not number!"
else:
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    result = template % (sum, sub, mul, div)
    message = result

print(message)