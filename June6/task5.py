
import random

def get_random_int(min, max):    
    result = random.random() * (max - min) + min
    return int(result)

print("Let's play game. You have to guess the number with 7 attempts. Good luck!")

def game():
    user_in = input("Your number from 0 tll 100:")
   
    try:
        num = int(user_in)
    except ValueError:
        print("Enter only number!")
        game()
    
    if my_random > num:
        print("Take bigger.")
        game()
    elif my_random < num:       
        print("Take smaller.")
        game()
    
    else:
        print("Congratulation! The random number was %d" % my_random)
        return

my_random = get_random_int (0, 100)
game()

answer = input("Would you like to play once more?")
if answer == "yes" or answer == "да":
    # VN: То же самое загаданное число остаётся
    game()

# Эту проверку: "Would you like to play once more?" нужно зациклить в рекурсивной функции.
# В ней же генерировать новое случайное число