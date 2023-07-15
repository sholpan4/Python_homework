#task2
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
        consonants = 'мл'
        if word[i] in vowels:
            syllable_word = word[i] + '-'
        elif word[i] in consonants:
            syllable_word = word[i] + '-' + word[i]
            # syllable_word += word[i+1]
        else:
            syllable_word += word[i]
    return syllable_word

def correct_syllables(word):
    new_word = ''
    for i in range(len(word)):
        if word[i].endswith('-'):
            new_word = '\n' + word[i]
    return ''.join(new_word)

new_text = list(map(get_syllables, text))
result = ''.join(new_text)
syllables = correct_syllables(result)

print(result)
print(syllables)    