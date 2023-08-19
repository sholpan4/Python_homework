# Сортировка "пузырьком"
#bubble_sort
user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

def bubblesort(elements):
    swapped = False
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]       
        if not swapped:
            return
 
# elements = [39, 12, 18, 85, 72, 10, 2, 18]

print("Sorted Array is, ")
result = bubblesort(my_list)
print(result)
    
    
    # while not is_sorted:
    #     is_sorted = True
    #     return is_sorted
    #     for i in range(len(the_list)-1):
    #         if the_list[i] > the_list[i+1]:
    #             the_list[i], the_list[i+1] = the_list[i+1], the_list[i]
    #             is_sorted = False
             
# print(my_list)