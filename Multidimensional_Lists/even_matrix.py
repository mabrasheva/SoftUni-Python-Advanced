"""
Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even.
Use nested comprehension for that problem.
On the first line, you will receive the rows of the matrix.
On the next rows, you will get elements for each column separated with a comma and a space ", ".
"""

import sys
from io import StringIO

test_input1 = """2
1, 2, 3
4, 5, 6
"""
test_input2 = """4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67
"""


# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def is_even(number):
    return number % 2 == 0


def matrix_even_numbers(matrix):
    # matrix_even_only = []
    # for row in matrix:
    #     matrix_even_only.append([i for i in row if is_even(i)])
    matrix_even_only = [[i for i in row if is_even(i)] for row in matrix]
    return matrix_even_only


rows_number = int(input())
matrix = [[int(i) for i in input().split(", ")] for _ in range(rows_number)]
result_matrix = matrix_even_numbers(matrix)
print(result_matrix)
