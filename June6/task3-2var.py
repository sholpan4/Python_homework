
num = int(input("Enter a number from 2 to 9:"))
def multipl_table():
    
    if (num < 1) or (num > 9):
        print("Error! Please enter a number from 2 to 9")
    else:
        for i in range(0, 11):
            
            return num * i
        multipl_table()

result = multipl_table() 
print(result)
