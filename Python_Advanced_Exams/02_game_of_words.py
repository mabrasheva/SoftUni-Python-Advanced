"""You will be given a string. Then, you will be given an integer N for the size of the field with square shape.
On the next N lines, you will receive the rows of the field. The player will be placed on a random position, marked
with "P". On random positions there will be letters. All the empty positions will be marked with "-".
Each turn you will be given commands for the player’s movement. If he moves to a letter, he consumes it, concatеnates
it to the initial string and the letter disappears from the field. If he tries to move outside the field, he is
punished - he loses the last letter in the string, if there are any, and the player’s position is not changed.
At the end print all letters and the field.
Input
•	On the first line, you are given the initial string
•	On the second line, you are given the integer N - the size of the square matrix
•	The next N lines holds the values for every row
•	On the next line you receive a number M
•	On the next M lines you will get a move command
Output
•	On the first line the final state of the string
•	In the end print the matrix
Constraints
•	The size of the square matrix will be between [2…10]
•	The player position will be marked with "P"
•	The letters on the field will be any letter except for "P"
•	Move commands will be: "up", "down", "left", "right"
"""
import sys
from io import StringIO

test_input1 = """Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right
"""
test_input2 = """Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left
"""


# sys.stdin = StringIO(test_input2)


def is_outside(row, column, size):
    return row < 0 or row >= size or column < 0 or column >= size


initial_string = input()
result_string = initial_string
size = int(input())
field = []
player_row, player_column = None, None
for row in range(size):
    line = list(input())
    field.append(line)
    if "P" in line:
        player_row = row
        player_column = line.index("P")
commands_count = int(input())
directions = {
    "up": lambda row, column: (row - 1, column),
    "down": lambda row, column: (row + 1, column),
    "left": lambda row, column: (row, column - 1),
    "right": lambda row, column: (row, column + 1),
}
for _ in range(commands_count):
    command = input()
    field[player_row][player_column] = "-"
    next_player_row, next_player_column = directions[command](player_row, player_column)
    if is_outside(next_player_row, next_player_column, size):
        if result_string:
            result_string = result_string[:-1]
    else:
        player_row, player_column = next_player_row, next_player_column
        if field[player_row][player_column].isalpha():
            result_string += field[player_row][player_column]
    field[player_row][player_column] = "P"

print(result_string)
for row in field:
    print("".join(row))
