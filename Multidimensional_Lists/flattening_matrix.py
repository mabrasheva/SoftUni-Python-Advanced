"""
Write a program that receives a matrix and prints the flattened version of it (a list with all the values).
For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
On the first line, you will receive the number of a matrix's rows. On the next rows, you will get the elements for each
column separated with a comma and a space ", ".
"""

# import sys
# from io import StringIO

# test_input = """3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99
# """

# sys.stdin = StringIO(test_input)

rows_number = int(input())
matrix = [[int(i) for i in input().split(",")] for _ in range(rows_number)]
flattening_matrix = [i for row in matrix for i in row]
print(flattening_matrix)
