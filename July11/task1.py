config = {}

cfg_file = open('url.ini', encoding='utf-8')
my_config = cfg_file.readlines()
cfg_file.close()

# current_section = ""
# my_config = ('https://www.google.com/search?q=palyndromes&rlz=1C1IXYC_ruKZ1059KZ1059&oq=&aqs=chrome.0.69i59i450l8.20045872j0j15&sourceid=chrome&ie=UTF-8')
print(my_config)
res = []

for sub in my_config.split(', '):
    if '=' in sub:
        res.append(map(str.strip, sub.split('=', 1)))
    res = dict(res)
    
print(+ str(res))



# for x in my_config:
#     # my_config = x.split('=')
#     my_config = x.split(':')
#     protocol = my_config[0]
#     # my_config = x.split('/')
#     domen = x[1].startswith('//') and x[1].endswith('com')
    
    
# print('протокол:', protocol, 'домен:', domen) 
   
# my_list = ['apple', 'banana', 'orange']

# my_string = ''

# for i, fruit in enumerate(my_list):

#  my_string += str(i) + ': ' + fruit + ', '

# # Remove the trailing comma and space

# my_string = my_string[:-2]

# print(my_string)

# Output: 0: apple, 1: banana, 2: orange