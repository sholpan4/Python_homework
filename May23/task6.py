#task6
film_name = input("Enter film name:")
cinema_name = input("Enter cinema name:")
user_in = input("Enter hours:")
hours = int(user_in)
user_in = input("Enter minutes:")
minutes = int(user_in)

template1 = "Film : %s"
message1 = template1 % film_name

template2 = "Cinema : %s"
message2 = template2 % cinema_name

template3 = "Time : %d hours" 
message3 = template3 % hours

template4 = ":%d minutes"
message4 = template4 % minutes

print(message1, message2, message3, message4)