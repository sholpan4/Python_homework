def process_large_file(file_path):
    total_lines = 0
    total_sums = 0
    
    with open(file_path, 'r') as fb:
        for line in fb:
            total_lines += 1
            numbers = [int(num) for num in line.split()]
            total_sums += sum(numbers)
            #VN: тут как раз нужен yield, который вернёт статистику по текущей строке
    return total_lines, total_sums

file_path = "October17Iteratior/task4.txt"  # не могу понять какие данные нужно передать. переданный текст не итерирует(
line_count, sum_of_numbers = process_large_file(file_path)

print(f"Total lines: {line_count}")
print(f"Sum of numbers in all lines: {sum_of_numbers}")