#task3
def multipl_table():
    table = ""
    for y in range(1, 11):
        for x in range(1,11):
            table += f' {x*y}\t'
        table += f'\n'
    return table

print(multipl_table())