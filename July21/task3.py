import random

def create_random_matrix(rows, cols):
    matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    r = 4
    c = 6

    random_matrix = create_random_matrix(r, c)
    print_matrix(random_matrix)