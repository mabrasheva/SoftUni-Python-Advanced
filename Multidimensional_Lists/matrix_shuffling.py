"""
Write a program that reads a matrix from the console and performs certain operations with its elements.
User input is provided similarly to the problems above - first, you read the dimensions and then the data.
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and
("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword along
with four valid coordinates (no more, no less), separated by a single space.
•	If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus,
you will be able to check if the operation was performed correctly).
•	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the
given coordinates are not valid), print "Invalid input!" and move on to the following command.
A negative value makes the coordinates not valid.
Your program should finish when the command "END" is entered.
"""

import sys
from io import StringIO

# test_input1 = """2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
# """
# test_input2 = """1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
# """
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def not_in_matrix(row, column, rows_count, columns_count):
    return row < 0 or column < 0 or row >= rows_count or column >= columns_count


def valid_command(command):
    valid = True
    if len(command) != 5 or command[0] != "swap":
        valid = False
        return valid
    row1, col1, row2, col2 = [int(i) for i in command[1::]]
    if not_in_matrix(row1, col1, rows_count, column_count) or not_in_matrix(row2, col2, rows_count, column_count):
        valid = False
    return valid


def swap_elements(row1, col1, row2, col2, matrix):
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for row in matrix:
        print(*row)


rows_count, column_count = [int(i) for i in input().split()]
matrix = [[i for i in input().split()] for row in range(rows_count)]

while True:
    command = input()

    if command == "END":
        break

    command = command.split()
    if not valid_command(command):
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(i) for i in command[1::]]
    swap_elements(row1, col1, row2, col2, matrix)
