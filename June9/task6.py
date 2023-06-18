#task6s
def get_tbl_ASCII():
    list(range(32, 127))
    for i in range(32, 127):
        print(chr(i), end=' ')
        if i % 5 == 0:
            print()
result = get_tbl_ASCII()            
print(result)