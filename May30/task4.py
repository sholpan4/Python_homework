#task4
user_in = input("Enter word with five letter:")
#word = user_in[::-1]

try:
    str = str(user_in)
    word = str[::-1]
except ValueError:
    message = "Please enter word with five letter!"

if user_in == word:
    message = "This word is a palindrome."
else:
    message = "This word is not a palindrome"

print(message)