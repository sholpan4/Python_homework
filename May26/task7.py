#task7
user_input1 = input("Enter hours: ")
user_input2 = input("Enter minutes: ")

try:
    hours = int(user_input1)
    minutes = int(user_input2)
    #23 60
except ValueError:
    message = "Error! You have entered not number!"
else:
    new_hours = 23 - hours
    new_minutes = 60 - minutes
    message = print(new_hours, "hours and", new_minutes, "minutes until the next day")
print(message)