#4. Расписание событий: Создайте программу для создания и
#отслеживания расписания событий с учетом времени.

import datetime

schedule = {}

def add_event(event, date_time):
    schedule[event] = date_time

def list_events():
    for event, date_time in schedule.items():
        print(f"{event} - {date_time('%Y-%m-%d %H:%M')}")  

def  main():
    while True:
        print("1. Add event")
        print("2. Show schedule")
        print("3. Exit")
        choice = input("Chose action:")

        if choice == "1":
            event = input("Enter the name of event: ")
            date_str = input("Enter date and time of event (yyyy-mm-dd  hh:mm): ")
            try:
                date_time = datetime.datetime.strftime(date_str, '%Y-%m-%d %H:%M') #подскажите как записать дату, время
                #VN:                   strptime  ^
                print("Event added.")
            except ValueError:
                print("Error: Wrong format of date and time.")

        elif choice == "2":
            list_events()
        elif choice == "3":
            break
        else:
            print("Wrong choice. Please, choose again.")

if __name__ == '__main__':
    main()

#VN: кажется, это неполное решение задачи