fruits = ['apple', 'banana', 'cherry', 'apple', 'orange', 'banana']
passed ={} #словарь, где будут пара из ключа и значения 

duplicates = [] #лист дубликатов 

for item in fruits: #если пары из списка fruits  
    if item in passed: #встретим в паре из словаря
        duplicates.append(item) #то пару сладываем в лист дубликатов
    else:
        passed[item] = True #иначе пары просто оставляем в словаре 
    
print(f'Найденные дубликаты: {duplicates}') #печатаем лист дубликатов