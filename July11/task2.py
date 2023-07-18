# from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# with open('mykey.key', 'wb') as mykey:
#     mykey.write(key)

text = 'SOS'
print(len(text))
result = [ord(text[0]), ord(text[1]), ord(text[2])]
print(result)

def get_letter(word):
    secret_txt = ''
#     # alph = 'OPQRSTUV'
#     # a = ord(word[0])
#     # b = ord(word[1])
#     # c = ord(word[2])
    for i in word:
        secret_txt += ord(word[i]+1)
    return secret_txt
       
     
# # print(text) 
print(get_letter(text))
# # result = list(filter(get_letter, text))   
# # print(result)