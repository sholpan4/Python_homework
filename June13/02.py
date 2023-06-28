class Calculator:
    color = " "
    model = " "
    digits = 0
    material = " "
    num1 = 0
    num2 = 0
        
    def __init__(self, color, model, digits, material):
        self.color = color
        self.model = model
        self.digits = digits
        self.material = material
        
    def __repr__(self) -> str:
        msg = "Calculator color: %s, model: %s, digits: %d, material: %s." % (self.color, self.model, self.digits, self.material)
        return msg 
    
    def get_addition(self, num1 = 0, num2 = 0):
        if num1:
            result = num1 + num2
            print("Result of addition of %.2f and %.2f is %.10f" % (num1, num2, result))
            
    def get_multiplication(self, num1 = 0, num2 = 0):
        if num1:
            result = num1 * num2
            print("Result of multiplication of %.2f and %.2f is %.10f" % (num1, num2, result))
            
    def get_division(self, num1 = 0, num2 = 0):
        if num1:
            result = num1 / num2
            print("Result of division of %.2f and %.2f is %.10f" % (num1, num2, result)) 
              
    def get_subtraction(self, num1 = 0, num2 = 0):
        if num1:
            result = num1 - num2
            print("Result of subtraction of %.2f and %.2f is %.10f" % (num1, num2, result))                                
            
first_calc = Calculator("black", "Citizen", 16, "plastic")
first_calc.get_addition(30.5, 20.2)
print(first_calc)

second_calc = Calculator("white", "Deli", 12, "policorbonate")
second_calc.get_division(40, 60)
print(second_calc)