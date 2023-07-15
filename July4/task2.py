#task2
from functools import reduce
# про-грам-ми-ро-ва-ни-е
# брил-ли-ант
# ба-ле-ри-на

my_file = open("text.txt", encoding="utf-8")
text = my_file.read()
my_file.close()
print(text)

def get_syllables(word):
    syllable_word = ''
    for i in range(len(word)):
        vowels = 'оаие'
        # consonants = 'мл' #как сделать чтобы двойные согласные переносились?
        if word[i] in vowels:
            syllable_word = word[i] + '-'  
        else:
            syllable_word += word[i]        
    return syllable_word

new_text = list(map(get_syllables, text))
result = ''.join(new_text)
# syllables = reduce(lambda acc , x: acc - x[i] if x[i].endswith('-') else acc, result)
#((( убрать дефис в конце как?
print(result)
# print(syllables)    