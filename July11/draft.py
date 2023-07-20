url= 'https://www.google.com/search?q=palyndromes&rlz=1C1IXYC_ruKZ1059KZ1059&oq=&aqs=chrome.0.69i59i450l8.20045872j0j15&sourceid=chrome&ie=UTF-8'
# protokol = url.split(':', 1)
def get_protokol(word):
    
    if word.endswith(':'):
        return word
    # return word

protokol = get_protokol(url)
print(f'Протокол: "{protokol}"')