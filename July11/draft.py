url= 'https://www.google.com/search?q=palyndromes&rlz=1C1IXYC_ruKZ1059KZ1059&oq=&aqs=chrome.0.69i59i450l8.20045872j0j15&sourceid=chrome&ie=UTF-8'
protokol_div = url.partition(':')
protokol = protokol_div[0]

domen_div = url.startswith('www') and url.endswith('com')

# def get_protokol(word):  
#     if word.endswith(':'):
#         return word
#     # return word

# protokol = get_protokol(url)
print(f"""Протокол: "{protokol}"
      Домен: "{domen_div}"
      Путь: ""
      Параметры запроса: ""
      """)