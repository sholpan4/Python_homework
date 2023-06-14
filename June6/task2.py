
def print_weekday(day=1):
    if day == 1:
        dayname = "Monday"
    elif day == 2:
        dayname = "Tuesday"
    elif day == 3:
        dayname = "Wednesday"
    elif day == 4:
        dayname = "Thursday"
    elif day == 5:
        dayname = "Friday"
    elif day == 6:
        dayname = "Saturday"
    elif day == 7:
        dayname = "Sunday"
    print("The day of the week is ", dayname)
    answer = input("Would you like to know next day?")
    if answer == "yes" or answer == "да":
        day += 1
        if day > 7:
            day = 1
        print_weekday(day)
print_weekday()