from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

# my_file = open('url.ini', encoding='utf-8')
# text = my_file.readlines()
# my_file.close()
# print(text)

