# Задание 2
#**Хэш-функции**
#Напишите программу, которая методом прямого перебора подберёт пароль, соответствующий хэшу MD5: 'f232b847c44bd9992dd04efe19597ee6'.
#Пароль имеет длину 8 символов, в пароле могут использоваться английские буквы в нижнем и верхнем регистре, цифры и спецсимволы из ряда: "~!@#$%^&*()_+-=".
#Измерьте время подбора пароля с помощью функции time() модуля time.

import hashlib


def chars_generate(find_hesh):
    with open('parol.txt') as file:
        password = file.readlines()
    for word in password:
        compare_hesh(find_hesh, word.strip())


def compare_hesh(input_md5, word):
    hash_word = hashlib.md5(word.encode('utf-8').strip()).hexdigest()
    print(hash_word)
    if input_md5 == hash_word:
        print(f'Пароль найден: {word}')
        exit(0)

def main():
    input_md5 = input('Введите хэшированный пароль: ')
    chars_generate(input_md5)

if __name__ == "__main__":
    main()