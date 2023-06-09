#task1
def get_num(num, num2):
    if num < num2:
        return -1
    elif num > num2:
        return 1
    else:
        return 0
    
num = get_num (10, 10)
print(num)