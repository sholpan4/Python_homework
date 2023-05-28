#task5
user_in = input("Enter word:")
my_symbol1 = user_in[0]
my_symbol2 = user_in[-1]
first_slice = user_in[1:-2] # VN: здесь неправильный второй индекс. Из-за этого "торт" превращается в "т*т"
                            # лучше всего было бы вычислить filler_length = len(user_in) - 2

len(first_slice)
filler = "*"
result = len (first_slice) * filler

word = my_symbol1+result+my_symbol2
print(word)