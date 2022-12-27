"""
Write a program that reads a number - N, representing the rows and columns of a square matrix.
On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters.
After that, you will receive a symbol.
Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})".
You should start searching from the top left.
If there is no such symbol, print the message "{symbol} does not occur in the matrix".
"""
#
# import sys
# from io import StringIO
#
# test_input1 = """3
# ABC
# DEF
# X!@
# !
# """
# test_input2 = """4
# asdd
# xczc
# qwee
# qefw
# 4
# """

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def find_symbol(matrix):
    size_matrix = len(matrix)
    for row_index in range(size_matrix):
        for column_index in range(size_matrix):
            if symbol == matrix[row_index][column_index]:
                return row_index, column_index


size_square_matrix = int(input())
square_matrix = [list(input()) for i in range(size_square_matrix)]
symbol = input()

if find_symbol(square_matrix):
    result = find_symbol(square_matrix)
    row, column = result
    print(f"({row}, {column})")
else:
    print(f"{symbol} does not occur in the matrix")
