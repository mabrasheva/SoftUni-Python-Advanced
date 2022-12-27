"""
Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with the biggest sum of its
values.
On first line you will get matrix sizes in format "{rows}, {columns}".  On the next rows, you will get elements for each
column, separated with a comma and a space ", ".
You should print the found submatrix and the sum of its elements, as shown in the examples.
•	Be aware of IndexError
•	If you find more than one max square, print the top-left one
"""
# import sys
# from io import StringIO
#
# test_input = """3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# """

# sys.stdin = StringIO(test_input)


def max_sum_submatrix(matrix, rows, columns):
    max_sum = 0
    submatrix_coordinates = []
    for row_index in range(rows - 1):
        for column_index in range(columns - 1):
            current_sum = matrix[row_index][column_index] + matrix[row_index + 1][column_index] + \
                          matrix[row_index][column_index + 1] + matrix[row_index + 1][column_index + 1]
            if current_sum > max_sum:
                max_sum = current_sum
                submatrix_coordinates = [row_index, column_index]
    sub_row_index, sub_column_index = submatrix_coordinates
    found_submatrix = [
        [matrix[sub_row_index][sub_column_index], matrix[sub_row_index][sub_column_index + 1]],
        [matrix[sub_row_index + 1][sub_column_index], matrix[sub_row_index + 1][sub_column_index + 1]]
    ]
    return found_submatrix, max_sum


rows_count, columns_count = [int(i) for i in input().split(", ")]
matrix = [[int(i) for i in input().split(", ")] for row in range(rows_count)]

submatrix, max_submatrix_sum = max_sum_submatrix(matrix, rows_count, columns_count)

for row in submatrix:
    print(*row)
print(max_submatrix_sum)
