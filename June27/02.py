names = ["Olessya", "Vasya", "Misha", "Tanya", "Aigerim", "Alexander", "Zhamilya"]

short_name = list(filter(lambda word: len(word) <= 7, names))

print(short_name)
# Используя функцию filter() печатайте только те имена, 
# у которых меньше 7 букв