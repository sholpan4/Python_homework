#task4
user_in = input("Enter word with five letter:")
#правда тут и с цифрами прокатывает)
try:
    str = str(user_in)
    word = str[::-1]
except ValueError:
    message = "Please enter word with five letter!"

if user_in == word:
    message = "This word is a palindrome."
elif len(user_in) < 5:
    message = "Please enter word with five letter!"
else:
    message = "This word is not a palindrome"

print(message)