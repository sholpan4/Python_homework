import random

def create_random_matrix(rows, cols):
    matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def odd_sum(matrix):
    row_sums = [sum(filter(lambda x: x % 2 != 0, row)) for row in matrix]
    col_sums = [sum(row[i] for row in matrix if row[i] % 2 != 0) for i in range(len(matrix[0]))]
    return row_sums, col_sums

if __name__ == "__main__":
    r = 4  # row
    c = 6  # column

    random_matrix = create_random_matrix(r, c)
    print("Matrix:")
    print_matrix(random_matrix)

    row_sums, col_sums = odd_sum(random_matrix)

    print("Sums of odd elements in each row:")
    for i, row_sum in enumerate(row_sums):
        print(f"Row {i + 1}: {row_sum}")

    print("Sums of odd elements in each column:")
    for i, col_sum in enumerate(col_sums):
        print(f"Column {i + 1}: {col_sum}")