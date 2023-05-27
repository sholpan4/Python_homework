#task9
user_in = input("Enter 5 digital number:")
num = int(user_in)

last_digit = num % 10
num = num // 10 
new_number = last_digit * 10000 + num

print(new_number)