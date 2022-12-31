"""Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its
elements. There will be no case with two or more 3x3 squares with equal maximal sum.
Input
•On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range
[1, 20]
•On the following lines, you will receive each row with its columns - integers, separated by a single space in the
range [-20, 20]
Output
•On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
•On the following 3 lines, print each element of the found submatrix, separated by a single space
"""


# import sys
# from io import StringIO
#
# test_input = """4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
# """
# sys.stdin = StringIO(test_input)


def max_sum(matrix, rows, columns, size_submatrix):
    biggest_sum = float("-inf")
    result_row = result_column = 0

    for row in range(rows - (size_submatrix - 1)):
        for column in range(columns - (size_submatrix - 1)):

            current_sum = 0
            for submatrix_row in range(row, row + size_submatrix):
                for submatrix_column in range(column, column + size_submatrix):
                    current_sum += matrix[submatrix_row][submatrix_column]

            if current_sum > biggest_sum:
                biggest_sum = current_sum
                result_row, result_column = row, column

    return biggest_sum, result_row, result_column


rows_count, columns_count = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for row in range(rows_count)]
size_of_submatrix = 3
result, result_row, result_column = max_sum(matrix, rows_count, columns_count, size_of_submatrix)

print(f"Sum = {result}")

for row in range(result_row, result_row + size_of_submatrix):
    sub_row = []
    for column in range(result_column, result_column + size_of_submatrix):
        sub_row.append(matrix[row][column])
    print(*sub_row)
