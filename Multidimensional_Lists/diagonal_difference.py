"""
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
On the first line, you will receive an integer N - the size of a square matrix.
The following N lines hold the values for each column - N numbers separated by a single space.
Print the absolute difference between the primary and the secondary diagonal sums.
"""


def primary_diagonal(matrix):
    size = len(matrix)
    primary_diagonal_elements = [matrix[i][i] for i in range(size)]
    sum_primary_diagonal_elements = sum(primary_diagonal_elements)
    return sum_primary_diagonal_elements


def secondary_diagonal(matrix):
    size = len(matrix)
    secondary_diagonal_elements = [matrix[i][size - i - 1] for i in range(size)]
    sum_secondary_diagonal_elements = sum(secondary_diagonal_elements)
    return sum_secondary_diagonal_elements


def diagonal_difference(matrix):
    return abs(primary_diagonal(matrix) - secondary_diagonal(matrix))


matrix_size = int(input())
matrix = [[int(i) for i in input().split()] for row in range(matrix_size)]
print(diagonal_difference(matrix))
