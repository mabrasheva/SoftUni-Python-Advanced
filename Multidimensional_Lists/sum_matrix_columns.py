"""
Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
On the first line, you will get matrix sizes in format "{rows}, {columns}".
On the next rows, you will get elements for each column separated with a single space.
Hints
•	Read matrix sizes.
•	On the next row lines, read the columns.
•	Traverse the matrix and sum all elements in each column.
•	Print the sum and continue with the other columns.
"""

# import sys
# from io import StringIO
#
# test_input = """3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
# """
# sys.stdin = StringIO(test_input)

row_count, column_count = [int(i) for i in input().split(", ")]
matrix = [[int(i) for i in input().split()] for row in range(row_count)]

for column_index in range(column_count):
    sum_column = 0
    for row_index in range(row_count):
        sum_column += matrix[row_index][column_index]
    print(sum_column)
