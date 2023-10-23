class MatrixIterator:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = 0
        self.col = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.row < len(self.matrix):
            if self.col < len(self.matrix[self.row]):
                result = self.matrix[self.row][self.col]
                self.col += 1
                return result
            else:
                self.row += 1
                self.col = 0
                return next(self)
        else:
            raise StopIteration

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __iter__(self):
        return MatrixIterator(self.matrix)
    
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# print(TypeError(matrix_data))
matrix = Matrix(matrix_data)

for element in matrix:
    print(element)