url= 'https://www.google.com/search?q=palyndromes&rlz=1C1IXYC_ruKZ1059KZ1059&oq=&aqs=chrome.0.69i59i450l8.20045872j0j15&sourceid=chrome&ie=UTF-8'
# protokol_div = url.partition(':')
# protokol = protokol_div[0]

def get_domen(url):
    cutted_url = ''
    for x in url:
        if x.starswith('www') and x.endswith('com'):
            cutted_url += x
            return cutted_url

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

print(get_domen(url))