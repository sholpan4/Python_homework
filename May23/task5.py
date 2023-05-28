#task5
user_in = input("Enter word:")
my_symbol1 = user_in[0]
my_symbol2 = user_in[-1]
first_slice = user_in[1:-2]

len(first_slice)
filler = "*"
result = len (first_slice) * filler

word = my_symbol1+result+my_symbol2
print(word)