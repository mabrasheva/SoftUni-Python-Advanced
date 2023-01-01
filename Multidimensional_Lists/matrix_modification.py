"""
Write a program that reads a matrix from the console and changes its values.
On the first line, you will get the matrix's rows - N.
You will get elements for each column on the following N lines, separated with a single space.
You will be receiving commands in the following format:
•	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
•	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates".
A coordinate is valid if both of the given indexes are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.
"""


def valid_coordinates(row, column, rows, columns):
    return (0 <= row < rows) and (0 <= column < columns)


rows_count = int(input())
matrix = [[int(i) for i in input().split()] for row in range(rows_count)]

while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    action = command[0]
    row, column, value = [int(i) for i in command[1::]]
    columns_count = len(matrix[0])
    if valid_coordinates(row, column, rows_count, columns_count):
        if action == "Add":
            matrix[row][column] += value
        elif action == "Subtract":
            matrix[row][column] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)
