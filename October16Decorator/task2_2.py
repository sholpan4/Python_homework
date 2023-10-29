from functools import lru_cache

class MathOperations:
    @lru_cache(maxsize=None)
    def calculate_square(self, number):
        print(f"Calculating square of {number}")
        return number * number

math = MathOperations()
result1 = math.calculate_square(5)
print(result1)

result2 = math.calculate_square(5)
print(result2)