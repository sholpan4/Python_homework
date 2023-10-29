import os


def get_files_in_directory_tree(root_directory):
    for files in os.walk(root_directory):
        for file in files:
            print(type(file)) #VN: посмотрите, что собой на самом деле
            print(file)       # представляет file
            yield os.path.join(file)
 
#root_directory = "October17Iteratior/task1.txt" #какой должен быть результат? не работает
root_directory = "." #VN: нужна ведь директория. Передадим текущую
for file_path in get_files_in_directory_tree(root_directory):
    print(file_path)
    

# tree = os.walk('task1')
# print(tree)

# for i in tree:
#     print(i)