#task1
def get_sum(num1, num2):
    sum = 0    
    for i in range(num1, num2 + 1):
        sum += i
    return sum

result = get_sum(5, 10)
print(result)