#task7
user_in1 = input("Enter circumference:")
user_in2 = input("Enter perimeter of the square:")

try:
    c = float(user_in1)
    p = float(user_in2)
    
    # VN: Остальные строки ислючений не сделают и не нужны в try 
    r = c / 6.28318
    s_circle = float(3.14159 * r)
    
    a = p / 4
    s_square = float(a ** 2)
    
except ValueError:
    c = ""
    p = ""
except NameError: #не получается поймать (((( 
    message = "Please enter number!"

# VN: здесь программа падает, если ввод некорректный. Нужна проверка c и p на пустые значения
if s_circle <= s_square:
    message = "This cirle can be fit into this square."
elif s_circle > s_square:
    message = "This cirlce can not be fit into this square."
else:
    message = "Please enter number!"
    
print(message)
    