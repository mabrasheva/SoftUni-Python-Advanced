"""You will be given an integer n for the size of the mines field with square shape and another one for the number of
bombs that you have to place in the field. On the next n lines, you will receive the position for each bomb. Your task
is to create the game field placing the bombs at the correct positions and mark them with "*", and calculate the numbers
in each cell of the field. Each cell represents a number of all bombs directly near it (up, down, left, right and the 4
diagonals).
Input
•	On the first line, you are given the integer n – the size of the square matrix.
•	On the second line – the number of the bombs.
•	The next n lines holds the position of each bomb.
Output
•	Print the matrix you've created.
Constraints
•	The size of the square matrix will be between [2…15].
"""


def is_inside(row, column, size):
    return 0 <= row and row < size and 0 <= column and column < size


def get_children(row, column, size):
    children_list = set()
    children = [
        (row - 1, column - 1),
        (row - 1, column),
        (row - 1, column + 1),
        (row, column - 1),
        (row, column + 1),
        (row + 1, column - 1),
        (row + 1, column),
        (row + 1, column + 1)
    ]
    for child_row, child_column in children:
        if is_inside(child_row, child_column, size):
            children_list.add((child_row, child_column))
    return children_list


def count_bombs_around(children_list, bombs_list):
    return len(bombs_list.intersection(children_list))


size = int(input())
bombs_number = int(input())

matrix = [[None for row in range(size)] for col in range(size)]

bombs_list = set()
for _ in range(bombs_number):
    bomb_row, bomb_column = [int(i) for i in input().lstrip("(").rstrip(")").split(", ")]
    bombs_list.add((bomb_row, bomb_column))

for row in range(size):
    for column in range(size):
        if (row, column) in bombs_list:
            matrix[row][column] = "*"
        else:
            children_cells_list = get_children(row, column, size)
            matrix[row][column] = count_bombs_around(children_cells_list, bombs_list)

for row in matrix:
    print(*row)
