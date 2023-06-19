

num = int(input("Enter at least two digit number:"))
n = int(input("How many digits to replace?"))
result = ""

def get_new_number():
    while num > 99:
        result = ""
        last_digit = num % 10
        num = num // 10
        new_num = last_digit * 10000 + num
        result += new_num
        return result
        recur(n-1)

msg = get_new_number()
print(msg)




