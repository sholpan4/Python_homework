#task9
def check_perfect_number(num):
    mylist = [2, 3, 5, 7, 13, 17, 19, 89, 107, 127]   
    for p in mylist:
        if 2 ** (p - 1) * (2 ** p -1) == num:
            print("%d is a perfect number!" % num)
            break
    else:
        print("This is not a perfect number!")
        
num = int(input("Enter the number:"))
check_perfect_number(num)