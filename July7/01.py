grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}

average_grade = sum(grades.values()) / len(grades) #для выявления среднего балла берем сумму всех значении и делим на количество значении, (85+92+78+90)/4

max_grade = max(grades.values()) #с помощью функиций макс выявили максимальное значение

print(f"Средний балл {average_grade}, максимальный {max_grade}") #принты