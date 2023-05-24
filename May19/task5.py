#task5 
def add(number1, number2):
    return number1 + number2
  
def subtract(number1, number2):
    return number1 - number2
  
def multiply(number1, number2):
    return number1 * number2
  
def divide(number1, number2):
    return number1 / number2
print("Please select operation: " 
        " 1. + " 
        " 2. - " 
        " 3. * " 
        " 4. / ")
 
select = int(input("Select operations form 1, 2, 3, 4 : "))
  
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
  
if select == 1:
    print(number1, "+", number2, "=",
                    add(number1, number2))
  
if select == 2:
    print(number1, "-", number2, "=",
                    subtract(number1, number2))
if select == 3:
    print(number1, "*", number2, "=",
                    multiply(number1, number2))
  
if select == 4:
    print(number1, "/", number2, "=",
                    divide(number1, number2))
else:
    print("Invalid input")