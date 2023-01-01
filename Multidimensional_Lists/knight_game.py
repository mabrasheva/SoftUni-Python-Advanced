"""
Chess is the oldest game, but it is still popular these days.
It will be used only one chess piece for this task - the Knight.
A chess knight has 8 possible moves it can make, as illustrated.
It can move to the nearest square but not on the same row, column, or diagonal. (e.g., it can move two squares
horizontally, then one square vertically, or it can move one square horizontally then two squares vertically -
i.e., in an "L" pattern.)
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells.
Your task is to remove knights until no knights that can attack one another with one move are left.
Always remove the knight who can attack the greatest number of knights.
If there are two or more knights with the same number of attacks, remove the top-left one.
Input
•	On the first line, you will receive integer N - the size of the board
•	On the following N lines, you will receive strings with "K" and "0"
Output
•	Print a single integer with the number of knights that need to be removed.
Constraints
•	The size of the board will be 0 < N < 30
•	Time limit: 0.3 sec. Memory limit: 16 MB
"""


def valid_coordinates(row, column, size):
    return (0 <= row < size) and (0 <= column < size)


def get_children_coordinates(row, column, size):
    valid_children = []
    possible_chilren = [
        [row - 2, column - 1],
        [row - 2, column + 1],
        [row - 1, column - 2],
        [row - 1, column + 2],
        [row + 1, column - 2],
        [row + 1, column + 2],
        [row + 2, column - 1],
        [row + 2, column + 1],
    ]
    for sub_row, sub_column in possible_chilren:
        if valid_coordinates(sub_row, sub_column, len(matrix)):
            valid_children.append([sub_row, sub_column])
    return valid_children


def attacked_number(row, column, matrix):
    count = 0
    for child_row, child_column in get_children_coordinates(row, column, len(matrix)):
        if matrix[child_row][child_column] == "K":
            count += 1
    return count


size = int(input())
matrix = [list(input()) for row in range(size)]

knights_to_remove = True
removed_knights = 0

while knights_to_remove:
    max_attacked = 0
    knight_row = knight_column = None
    for row in range(size):
        for column in range(size):
            if matrix[row][column] == "K":
                attacked_count = attacked_number(row, column, matrix)
                if attacked_count > max_attacked:
                    max_attacked = attacked_count
                    knight_row = row
                    knight_column = column

    if max_attacked > 0:
        matrix[knight_row][knight_column] = "0"
        removed_knights += 1
    else:
        knights_to_remove = False

print(removed_knights)
