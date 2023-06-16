num = int(input("Enter a number from 2 to 9:"))
if (num < 1) or (num > 9):
    print("Error! Please enter a number from 2 to 9")
else:
    for i in range(0, 11):
        sum = num * i
        print(num, "*", i, "=", sum)