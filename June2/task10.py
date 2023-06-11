#task10
def check_perfect_number(num, num2):
    for i in range(num, num2):    
        mylist = [2, 3, 5, 7, 13, 17, 19, 89, 107, 127]   
        for p in mylist:
            if 2 ** (p - 1) * (2 ** p -1) == i:
                print("%d is a perfect number!" % i)
                break           
        
num = int(input("Enter the minumum number:"))
num2 = int(input("Enter the maximum number:"))
check_perfect_number(num, num2)