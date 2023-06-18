
list_num = [int(input("Enter 10 numbers with "," "))]

def check_list(list_num):
    result = 0
    index = 0
    count_pos = 0
    count_neg = 0
    count_even = 0
    count_odd = 0
    count_zero = 0
    
    for x in range(list_num):
        if x % 2 == 0:
            count_even += 1
            result += x
        else:
            count_odd += 1
            result += x
        if x < 0:
            count_pos += 1
            result += x
        else:
            count_neg += 1
            result += x
        if x == 0:
            count_zero +=1
            result += x
    return result

msg = check_list(list_num)
print(msg)