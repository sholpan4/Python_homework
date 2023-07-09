#task3
my_list = [3, 9, 8, 4, 5, 1]

list_max = max(my_list)
list_min = min(my_list)

a = my_list.index(list_max)
b = my_list.index(list_min)

first = my_list.pop(a)
second = my_list.pop(b-1)

add_list_1 = my_list.insert(a, list_min)
add_list_2 = my_list.insert(b, list_max)

print(my_list)