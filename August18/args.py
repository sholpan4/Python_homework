
def my_sum(num, *args, **kwargs):
    result = num
    print(args);
    print(kwargs)
    for x in args:
        result += x
    if 'negative' in kwargs:
        if kwargs['negative'] == True:
            result = -result
    return result

day = 3
print(my_sum(5, 8, 8, 43, 3, 100, reverse=True, negative=True))
print(my_sum(2))

print("Текущий день недели:", day)