"""You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a
new line. On the last line of input, you will receive indexes - coordinates of several cells separated by a single
space, in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
On those cells, there are bombs. You must detonate every bomb in the order they were given. When a bomb explodes, it
deals damage equal to its integer value to all the surrounding cells (in every direction and in all diagonals).
One bomb can't explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or below,
it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells (including the
dead ones).
Input
•	On the first line, you are given the integer N - the size of the square matrix.
•	The following N lines hold each column's values - N numbers separated by a space.
•	On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
Output
•	On the first line, you need to print the count of all alive cells in the format:
"Alive cells: {alive_cells}"
•	On the second line, you need to print the sum of all alive cells in the format:
"Sum: {sum_of_cells}"
•	In the end, print the matrix. A space must separate the cells.
Constraints
•	The size of the matrix will be between [0…1000].
•	The bomb coordinates will always be in the matrix.
•	The bomb's values will always be greater than 0.
•	The integers of the matrix will be in the range [1…10000].
"""

from collections import deque


def not_in_matrix(row, column, size_matrix):
    return row < 0 or column < 0 or row >= size_matrix or column >= size_matrix


def get_children(row, column, matrix):
    possible_children = [
        [row - 1, column - 1],
        [row - 1, column],
        [row - 1, column + 1],
        [row, column - 1],
        [row, column + 1],
        [row + 1, column - 1],
        [row + 1, column],
        [row + 1, column + 1],
    ]
    children = []
    for child_row, child_column in possible_children:
        if not_in_matrix(child_row, child_column, len(matrix)):
            continue
        children.append([child_row, child_column])
    return children


def explode_bomb(row, column, matrix):
    children_cells = get_children(row, column, matrix)
    bomb_power = matrix[row][column]
    matrix[row][column] = 0  # bomb coordinates
    for child_row, child_column in children_cells:
        # When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
        if matrix[child_row][child_column] > 0:
            matrix[child_row][child_column] -= bomb_power


size_square_matrix = int(input())
matrix = [[int(i) for i in input().split()] for row in range(size_square_matrix)]
bombs_coordinates = deque(input().split())

while bombs_coordinates:
    coordinates = bombs_coordinates.popleft().split(",")
    row, column = [int(i) for i in coordinates]
    if matrix[row][column] <= 0:  # bomb power should be positive integer
        continue
    explode_bomb(row, column, matrix)

alive_cells = 0
sum_alive_cell = 0
for row in range(len(matrix)):
    for column in range(len(matrix)):
        current_cell = matrix[row][column]
        if current_cell > 0:
            alive_cells += 1
            sum_alive_cell += current_cell

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive_cell}")
for row in matrix:
    print(*row)
