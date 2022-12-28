"""
Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a
comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".
"""

# import sys
# from io import StringIO
#
# test_input = """3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# """
# sys.stdin = StringIO(test_input)


def primary_diagonal(matrix):
    size = len(matrix)
    primary_diagonal_elements = [matrix[i][i] for i in range(size)]
    sum_primary_diagonal_elements = sum(primary_diagonal_elements)
    primary_diagonal_elements_formatted = ', '.join([str(i) for i in primary_diagonal_elements])
    print(f"Primary diagonal: {primary_diagonal_elements_formatted}. Sum: {sum_primary_diagonal_elements}")


def secondary_diagonal(matrix):
    size = len(matrix)
    secondary_diagonal_elements = [matrix[i][size - i - 1] for i in range(size)]
    sum_secondary_diagonal_elements = sum(secondary_diagonal_elements)
    primary_diagonal_elements_formatted = ', '.join([str(i) for i in secondary_diagonal_elements])
    print(f"Secondary diagonal: {primary_diagonal_elements_formatted}. Sum: {sum_secondary_diagonal_elements}")


matrix_size = int(input())
matrix = [[int(i) for i in input().split(", ")] for row in range(matrix_size)]
primary_diagonal(matrix)
secondary_diagonal(matrix)
