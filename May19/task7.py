user_in = input("Enter hours: ")
hours = int(user_in)

user_in = input("Enter minutes: ")
minutes = int(user_in)

#23 60
new_hours = 23 - hours
new_minutes = 60 - minutes

print(new_hours, "hours and", new_minutes, "minutes until the next day")