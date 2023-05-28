#task9
string = input("Enter text:")
user_in = input("How many time repeat:")
repeats = int(user_in)

result = string * repeats
template = "Result: %s"

message = template % result 
print(message)