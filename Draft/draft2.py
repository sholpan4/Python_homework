num = int(input("Enter a number from 2 to 9:"))
def multipl_table():
    
    if (num < 1) or (num > 9):
        print("Error! Please enter a number from 2 to 9")
    else:
        num = int
        for i in range(0, 11):
            
            num *= i
            return num
        #multipl_table()

result = multipl_table() 
print(result)
