#task2
def get_GCD(a, b):
    if a > b:
        temp = b
    else:
        temp = a
    
    for i in range(1, temp +1):
        if ((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

num = get_GCD(num1, num2)
print("GCD of two number is: %s" % num)
