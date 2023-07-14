#task1
user_in = input('Please enter list of ten numbers with ",":')
user_list = user_in.split(",")

# print(user_list)
lenght = len(user_list)

#VN: Здесь сразу можно проверить: if length < 10 и сообщить ему, что нужно 10 чисел
# А лучше сделать так:
# length = 0
# while lenght < 10:
#     user_in = input('Please enter list of ten numbers with ",":')
#     user_list = user_in.split(",")
#     lenght = len(user_list)

for i in range(lenght):
    user_list[i] = int(user_list[i])
    
    if lenght == 10: #VN: для этой проверки есть всё необходимое ещё до цикла. см. выше
        new_list = []
        for i in range(lenght): #VN: Этот цикл не нужен
            if user_list[i] % 2:
                continue
            else:
                new_list.append(user_list[i])
                
        msg = new_list #не получается(
                       #VN: второй цикл мешает
        
        # msg = user_list
    elif lenght > 10:
        msg = user_list[0: 10]
    else:
        msg = "Please enter ten numbers."        
     
# msg = list(map(lambda x: x % 2 == 0, msg))
#VN:         ^^^ здесь filter как раз подойдёт. И тогда с 16 по 34 строку всё можно убрать

print(msg)