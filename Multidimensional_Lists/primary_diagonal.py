"""
Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
On the first line, you will receive an integer N – the size of a square matrix.
The next N lines holds the values for each column - N numbers, separated by a single space.
"""
# import sys
# from io import StringIO
#
# test_input = """3
# 11 2 4
# 4 5 6
# 10 8 -12
# """

# sys.stdin = StringIO(test_input)


def sum_primary_diagonal(size_n, matrix):
    # sum_diagonal = 0
    # for row in range(size_n):
    #     for column in range(size_n):
    #         if row == column:
    #             sum_diagonal += matrix[row][column]
    # return sum_diagonal
    return sum(matrix[i][i] for i in range(size_n))


size_of_square_matrix = int(input())
square_matrix = [[int(i) for i in input().split()] for _ in range(size_of_square_matrix)]
print(sum_primary_diagonal(size_of_square_matrix, square_matrix))
