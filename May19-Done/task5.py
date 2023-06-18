#task5 
user_in1 = input("Enter first number: ")
user_in2 = input("Enter second number: ")

template = """
Addition:       %.2f
Subtraction:    %.2f
Multiplication: %.2f
Division:       %.2f
""" 

num1 = float(user_in1) 
num2 = float(user_in2)

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
message = template % (sum, sub, mul, div)

print(message)