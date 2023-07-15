my_file = open("text.txt", encoding="utf-8")
text = my_file.read()
my_file.close()
print(text)


def syllable_split(word):
    count = 0
    
    vowels = 'оаие'
    syll = ''
    temp = 0
    for letter in word:
        if letter in vowels:
            count += 1
    if count == 1:
        return word
    for index in range(count, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            w = word[temp: index - 1]
            if len(w) != 0:
                syll += w
                temp = index - 1
    return syll


print(syllable_split(text))