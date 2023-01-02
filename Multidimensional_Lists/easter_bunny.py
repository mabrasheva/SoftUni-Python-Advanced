"""
Your task is to collect as many eggs as possible.
On the first line, you will be given a number representing the size of the field.
On the following few lines, you will be given a field with:
•	One bunny - randomly placed in it and marked with the symbol "B"
•	Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
The directions that should be considered as possible are up, down, left, and right.
If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this
direction. For more clarifications, see the examples below.
Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
Input
•	A number representing the size of the field
•	The matrix representing the field (each position separated by a single space)
Output
•	The direction which should be considered as best (lowercase)
•	The field positions from which we are collecting eggs as lists
•	The total number of eggs collected
Constraints
•	There will NOT be two or more paths consisting of the same total amount of eggs.
"""

# import sys
# from io import StringIO

# test_input3 = """5
# B -3 X 9 11
# 0 5 4 X 63
# X 3 21 95 1
# 0 1 73 4 9
# 9 2 33 2 0
# """

# sys.stdin = StringIO(test_input3)

def bunnie_position(size_matrix):
    for row in range(size_matrix):
        for column in range(size_matrix):
            if matrix[row][column] == "B":
                return row, column


def get_children(direction, bunnie_row, bunnie_column, size):
    children = []
    current_sum = 0
    row, column = 0, 0

    if direction == "right":
        row, column = 0, 1
    elif direction == "left":
        row, column = 0, -1
    elif direction == "up":
        row, column = -1, 0
    elif direction == "down":
        row, column = 1, 0

    for _ in range(size):
        bunnie_row += row
        bunnie_column += column
        if 0 <= bunnie_row < size and 0 <= bunnie_column < size:
            if matrix[bunnie_row][bunnie_column] == "X":
                break
            if int(matrix[bunnie_row][bunnie_column]) >= 0:
                children.append([bunnie_row, bunnie_column])
                current_sum += int(matrix[bunnie_row][bunnie_column])

    return children, current_sum


size_matrix = int(input())
matrix = []
for row in range(size_matrix):
    matrix.append([i for i in input().split()])

bunnie_row, bunnie_column = bunnie_position(size_matrix)
directions = ["right", "left", "up", "down"]
best_direction = ""
max_sum = float("-inf")
steps = []
for direction in directions:
    children, current_sum = get_children(direction, bunnie_row, bunnie_column, size_matrix)
    if current_sum > max_sum and children:
        max_sum = current_sum
        best_direction = direction
        steps = children

print(best_direction)
for element in steps:
    print(element)
print(max_sum)
