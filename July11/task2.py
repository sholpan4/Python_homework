# from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# with open('mykey.key', 'wb') as mykey:
#     mykey.write(key)

text = 'SOS'

def get_letter(word):
    secret_txt = ''
    alph = 'OPQRSTUV'
    for i in range(len(alph)):
        if word in alph:
            secret_txt += alph[i + 1]
        return secret_txt
     
print(text) 
print(get_letter(text))
result = list(filter(get_letter, text))   
print(result)