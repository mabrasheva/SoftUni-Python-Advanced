"""
Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in
the examples below.
•	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
•	Columns + rows define the middle letter:
o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
Input
•	The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
•	r and c are integers in the range [1, 26]
"""


def matrix_of_palindromes(rows, columns):
    symbol = 97
    result_matrix = []
    for row_index in range(rows):
        row = []
        for columns_index in range(columns):
            palindrome = chr(row_index + symbol) + chr(row_index + columns_index + symbol) + chr(row_index + symbol)
            row.append(palindrome)
        result_matrix.append(row)
    return result_matrix


rows_count, columns_count = [int(i) for i in input().split()]
# rows_count, columns_count = 4, 6
matrix_of_palindromes(rows_count, columns_count)
result = matrix_of_palindromes(rows_count, columns_count)

for row_index in range(len(result)):
    print(*result[row_index])
