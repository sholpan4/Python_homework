#task8
user_in = input("Введите трехзначное число: ")
try:
    num = int(user_in)
except ValueError:
    message = "Error! You have entered not number!"    
else:  
    my_slice = user_in[1]
    
    message = "%s" % my_slice
print(message)