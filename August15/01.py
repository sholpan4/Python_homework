# Сортировка "пузырьком"
#bubble_sort
user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

def bubble_sort(the_list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(the_list)-1):
            if the_list[i] > the_list[i+1]:
                the_list[i], the_list[i+1] = the_list[i+1], the_list[i]
                is_sorted = False

print(bubble_sort(my_list))
# print(my_list)