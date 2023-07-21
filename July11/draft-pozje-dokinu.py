# config = {}

# cfg_file = open('url.ini', encoding='utf-8')
# my_config = cfg_file.readlines()
# cfg_file.close()

# current_section = ""
my_config = 'https://www.google.com/search?q=palyndromes&rlz=1C1IXYC_ruKZ1059KZ1059&oq=&aqs=chrome.0.69i59i450l8.20045872j0j15&sourceid=chrome&ie=UTF-8'
print(my_config)
# res = []

# for sub in my_config.split(' '):
#     if '=' in sub:
#         res.append(map(my_config.strip, sub.split('=', 1)))
#     res = dict(res)
    
# print(str(res))



for x in my_config:
    # my_config = x.split('=')
    my_config = x.split(':')
    protocol = my_config[0]
    # my_config = x.split('/')
    domen = my_config[1].startswith('//') + my_config[1].endswith('com')
    
    
print('протокол:', protocol, 'домен:', domen) 
   
# my_list = ['apple', 'banana', 'orange']

# my_string = ''

# for i, fruit in enumerate(my_list):

#  my_string += str(i) + ': ' + fruit + ', '

# # Remove the trailing comma and space

# my_string = my_string[:-2]

# print(my_string)

# Output: 0: apple, 1: banana, 2: orange


# url= 'https://www.google.com/search?q=palyndromes&rlz=1C1IXYC_ruKZ1059KZ1059&oq=&aqs=chrome.0.69i59i450l8.20045872j0j15&sourceid=chrome&ie=UTF-8'
# protokol_div = url.partition(':')
# protokol = protokol_div[0]


# def get_domen(url):
#     domen = ''
#     for i in range(len(url)):
#         if i == '/':
#             domen += url
#             return domen

# def get_protokol(word):  
#     if word.endswith(':'):
#         return word
#     # return word

# protokol = get_protokol(url)
# print(f"""
#       Протокол: "{protokol}"
#       Домен: "{domen_div}"
#       Путь: ""
#       Параметры запроса: ""
#       """)

# print(get_domen(url))