#task9
user_in = input("Enter 5 digital number:")
try:
    num = int(user_in)
except ValueError:
    message = "Error! You have entered not number!"
else:    
    last_digit = num % 10
    num = num // 10 
    new_number = last_digit * 10000 + num
    message = new_number

print(message)