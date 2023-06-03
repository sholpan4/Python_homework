#task4
user_in = str(input("Enter word with five letter:"))
word = user_in[::-1]

if user_in == word:
    message = "This word is a palindrome."
else:
    message = "This word is not a palindrome"

print(message)