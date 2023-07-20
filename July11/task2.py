my_file = open('encrypt-text.txt', encoding="utf-8")
text = my_file.read()
my_file.close()

def get_secret_word(word):
    secret_ord = ''
    for i in range(len(word)):
        num = ord(word[i]) + 1
        letter = chr(num)
        secret_ord += letter
    return secret_ord

secert_num = get_secret_word(text)
print(secert_num)