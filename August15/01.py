# Сортировка "пузырьком"
#bubble_sort
user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

def bubble_sort(num_list, key = None):
    for n in range(len(num_list)-1):
        counter = 0
        for i in range(len(num_list)-1):
            if num_list[i] > num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                counter += 1
        if counter == 0:
            break
    # return num_list
        continue
    
    if key:
        new_list = []
        for i in range(len(num_list)):
            if key(num_list[i]):
                new_list.append(num_list[i]) # не получается додумать
            elif not key(num_list[i]):
                
    else:
        return num_list
               
print(bubble_sort(my_list))
print(bubble_sort(my_list, key=lambda x: x ** 2))

# is_sorted = False
    # while not is_sorted:
    #     is_sorted = True
    #     for i in range(len(my_list)-1):
    #         if my_list[i] > my_list[i+1]:
    #             my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    #             is_sorted = False