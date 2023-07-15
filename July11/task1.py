config = {}

cfg_file = open('url.ini', encoding='utf-8')
my_config = cfg_file.readlines()
cfg_file.close()

print(my_config)
# current_section = ""

for x in my_config:
    # my_config = x.split('=')
    my_config = x.split(':')
    protocol = my_config[0]
    my_config = x.split('/')
    domen = my_config[1].startswith('/')
    
    
print('протокол:', protocol, 'домен:', domen)    