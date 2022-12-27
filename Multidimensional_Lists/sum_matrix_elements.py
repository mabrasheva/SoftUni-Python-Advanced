# Write a program that reads a matrix from the console and prints:
# •	The sum of all numbers in the matrix
# •	The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated by a comma and a space ", ".

# import sys
# from io import StringIO
#
# test_input = """3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# """
# sys.stdin = StringIO(test_input)


def sum_matrix(matrix, row_count):
    total = 0
    for row_index in range(row_count):
        total += sum([i for i in matrix[row_index]])
    return total


row_count, column_count = [int(i) for i in input().split(", ")]
# matrix = [[int(i) for i in input().split(", ")] for row in range(row_count)]
matrix = []
for row_index in range(row_count):
    matrix.append([int(i) for i in input().split(", ")])

total_sum = sum_matrix(matrix, row_count)

print(total_sum)
print(matrix)
