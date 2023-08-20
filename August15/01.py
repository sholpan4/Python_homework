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
    return num_list
    
print(bubble_sort(my_list))