"""You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M.
A string represents the snake. It starts moving from the top-left corner to the right.
When the snake reaches the end of the row, it slithers its way down to the next row and turns left.
The moves are repeated to the very end.
The first cell is filled with the first symbol of the snake. The second cell is filled with the second symbol, etc.
The snake's path is as long as it takes to fill the matrix completely - if you reach the end of the string representing
the snake, start again at the first symbol. In the end, you should print the snake's path.
Input
The input data consists of exactly two lines:
•	On the first line, you will receive the dimensions N x M of the field in format: "{rows} {columns}".
•	On the second line, you will receive the string representing the snake
Output
•	You should print the snake's zigzag path of size N x M (rows x columns)
Constraints
•	The dimensions N and M of the matrix will be integers in the range [1 … 12]
•	The snake will be a string with length in the range [1 … 20] and will not contain any whitespace characters
"""

# import sys
# from io import StringIO
#
# test_input = """5 6
# SoftUni
# """
# sys.stdin = StringIO(test_input)

### Version 1:
# rows_count, columns_count = [int(i) for i in input().split()]
# word = input()
# matrix = [[None for i in range(columns_count)] for row in range(rows_count)]
#
# index = 0
# for row in range(rows_count):
#     if row % 2 == 0:
#         for column in range(columns_count):
#             matrix[row][column] = word[index % len(word)]
#             index += 1
#     else:
#         for column in range(columns_count - 1, -1, -1):
#             matrix[row][column] = word[index % len(word)]
#             index += 1
#
# for row in matrix:
#     print(*row, sep="")

### Version 2:
from collections import deque

rows_count, columns_count = [int(i) for i in input().split()]
word = deque(input())
matrix = [[None for i in range(columns_count)] for row in range(rows_count)]
for row in range(rows_count):
    if row % 2 == 0:
        for column in range(columns_count):
            symbol = word.popleft()
            matrix[row][column] = symbol
            word.append(symbol)
    else:
        for column in range(columns_count-1, -1, -1):
            symbol = word.popleft()
            matrix[row][column] = symbol
            word.append(symbol)

for row in matrix:
    print(*row, sep="")
