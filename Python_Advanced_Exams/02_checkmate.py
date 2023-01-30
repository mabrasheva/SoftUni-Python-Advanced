"""You will be given a chess board (8x8). On the board there will be 3 types of symbols:
•	"." – empty square
•	"Q" – a queen
•	"K" – the king
Your job is to find which queens can capture the king and print them.
The moves that the queen can do is to move diagonally, horizontally and vertically (basically all the moves that all
the other figures can do except from the knight). Beware that there might be queens that stand in the way of other
queens and can stop them from capturing the king. For more clarification see the examples.
Input
•	8 lines – the state of the board (each square separated by single space)
Output
•	The positions of the queens that can capture the king as lists
•	If the king cannot be captured, print: "The king is safe!"
•	The order of output does not matter
Constrains
•	There will always be exactly 8 lines
•	There will always be exactly one King
•	Only the 3 symbols described above will be present in the input
"""

import sys
from io import StringIO

test_input1 = """. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .
"""
test_input2 = """. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . .
"""


# sys.stdin = StringIO(test_input1)


def is_inside(row, column, size):
    return 0 <= row < size and 0 <= column < size


def check_capture(king_row, king_column, queens, directions):
    queens_that_can_capture = []
    for direction in directions:
        test_king_row, test_king_column = king_row, king_column
        while is_inside(test_king_row, test_king_column, size):
            test_king_row, test_king_column = directions[direction](test_king_row, test_king_column)
            if [test_king_row, test_king_column] in queens:
                queens_that_can_capture.append([test_king_row, test_king_column])
                break
    return queens_that_can_capture


size = 8
matrix = []
king_row, king_column = None, None
queens = []
for row in range(size):
    line = input().split()
    matrix.append(line)

    for index, element in enumerate(line):
        if element == "K":
            king_row = row
            king_column = index
        elif element == "Q":
            queens.append([row, index])

directions = {
    "up": lambda row, column: (row - 1, column),
    "down": lambda row, column: (row + 1, column),
    "left": lambda row, column: (row, column - 1),
    "right": lambda row, column: (row, column + 1),
    "diagonal_left_up": lambda row, column: (row - 1, column - 1),
    "diagonal_right_up": lambda row, column: (row - 1, column + 1),
    "diagonal_left_down": lambda row, column: (row + 1, column - 1),
    "diagonal_right_down": lambda row, column: (row + 1, column + 1),
}

queens_result = check_capture(king_row, king_column, queens, directions)

if queens_result:
    print(*queens_result, sep="\n")
else:
    print("The king is safe!")
