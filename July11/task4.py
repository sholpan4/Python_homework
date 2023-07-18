text = 'Вddd сssssтроке удалить идущие подряд символы'

def f(word):
    out = ''
    for i in range(len(word)-1):
        if word[i] != word[i + 1]:
            out += word[i]
    if word[-1] != out[-1]:
        out += word[-1]
    return out

print(f(text))