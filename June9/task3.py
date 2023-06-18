#task3
num = int(input("Enter number:"))
counter = 0

while num > 50: 
    num /= 2
    counter += 1
    print(num)
print("The end. %d times divided" % counter)