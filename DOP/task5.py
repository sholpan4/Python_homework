import random

def create_random_matrix(rows, cols):
    matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def find_max_min_elements(matrix):
    max_in_rows = [max(row) for row in matrix]
    min_in_rows = [min(row) for row in matrix]
    
    max_in_cols = [max(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
    min_in_cols = [min(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0])]

    return max_in_rows, min_in_rows, max_in_cols, min_in_cols

if __name__ == "__main__":
    r = 4
    c = 6 

    random_matrix = create_random_matrix(r, c)
    print("Matrix:")
    print_matrix(random_matrix)

    max_in_rows, min_in_rows, max_in_cols, min_in_cols = find_max_min_elements(random_matrix)

    print("Maximum elements in each row:")
    for i, max_val in enumerate(max_in_rows):
        print(f"Row {i + 1}: {max_val}")

    print("Minimum elements per line:")
    for i, min_val in enumerate(min_in_rows):
        print(f"Row {i + 1}: {min_val}")

    print("Maximum elements in each column:")
    for i, max_val in enumerate(max_in_cols):
        print(f"Column {i + 1}: {max_val}")

    print("Minimum elements in each column:")
    for i, min_val in enumerate(min_in_cols):
        print(f"Column {i + 1}: {min_val}")