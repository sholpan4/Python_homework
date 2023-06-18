#task3
user_in = input("Enter a year:")

try:
    year = int(user_in)
except ValueError:
    message = "Please enter a year in numbers!"
except TypeError:
    message = "You've entered not a number!"
except NameError:
    message = "You've entered not a number!" #не получается словить (((

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    message = "This is the leap year"
else:
    message = "This is not the leap year!"

print(message)