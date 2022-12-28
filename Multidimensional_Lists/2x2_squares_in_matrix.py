"""
Find the number of all 2x2 squares containing identical chars in a matrix.
On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}".
On the following rows, you will receive characters separated by a single space.
Print the number of all square matrices you have found.
"""


# import sys
# from io import StringIO

# test_input1 = """3 4
# A B B D
# E B B B
# I J B B
# """
# test_input2 = """2 2
# a b
# c d
# """
# test_input3 ="""5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P
# """
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

def square_matrix_count(matrix, rows, columns):
    counter = 0
    for row_index in range(rows - 1):
        for column_index in range(columns - 1):
            if matrix[row_index][column_index] == matrix[row_index + 1][column_index] == \
                    matrix[row_index][column_index + 1] == matrix[row_index + 1][column_index + 1]:
                counter += 1
    return counter


rows_count, columns_count = [int(i) for i in input().split()]
matrix = [input().split() for row in range(rows_count)]
print(square_matrix_count(matrix, rows_count, columns_count))
