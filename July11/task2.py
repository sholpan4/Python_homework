text = 'SOS'
print(len(text))
result = ord(text[0]), ord(text[1]), ord(text[2])
print(result)

def get_ord(word):
    secret_ord = ''
    for i in range(len(word)):
        a = str(ord(word[i]) + 1)
        secret_ord += a + ' '
    return secret_ord

secert_num = get_ord(text)
print(secert_num)
num = secert_num.strip(' ')
print(num)

def get_secret_letter(numbers):
    secret_txt = ''
    for x in numbers:
        letter = chr(x)
        secret_txt += letter
    return secret_txt

secret_text = get_secret_letter(num)
print(secret_text)