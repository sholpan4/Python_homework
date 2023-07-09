#task1
user_in = input('Please enter list of ten numbers with ",":')
user_list = user_in.split(",")

# print(user_list)
lenght = len(user_list)

for i in range(lenght):
    user_list[i] = int(user_list[i])
    
    if lenght == 10:
        new_list = []
        for i in range(lenght):
            if user_list[i] % 2:
                continue
            else:
                new_list.append(user_list[i])
                
        msg = new_list #не получается(
        
        # msg = user_list
    elif lenght > 10:
        msg = user_list[0: 10]
    else:
        msg = "Please enter ten numbers."        
     
# msg = list(map(lambda x: x % 2 == 0, msg))

print(msg)