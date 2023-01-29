"""On the first line, you will be given a number representing the size of the field with a square shape. On the
following few lines, you will be given the field with:
•	One player - randomly placed in it and marked with the symbol "P"
•	Numbers for coins placed at different positions of the field
•	Walls marked with "X"
After the field state, you will be given commands for the player's movement. Commands can be: "up", "down", "left",
"right". If the command is invalid, you should ignore it.
The player moves in the given direction with one step for each command and collects all the coins that come across.
If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
Note: He can go through the same path many times, but he can collect the coins just once (the first time).
There are only two possible outcomes of the game:
•	The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest number.
•	The player collects at least 100 coins and wins the game.
For more clarifications, see the examples below.
Input
•	A number representing the size of the field (matrix NxN)
•	A matrix representing the field (each position separated by a single space)
•	On each of the following lines, you will get a move command.
Output
•	If the player won the game, print: "You won! You've collected {total_coins} coins."
•	If the player loses the game, print: "Game over! You've collected {total_coins} coins."
•	Collected coins have to be rounded down to the next-lowest number.
•	The player's path as cooridnates in lists on separate lines:
"Your path:
[{row_position1}, {column_position1}]
[{row_position2}, {column_position2}]
…
[{row_positionN}, {column_positionN}]"
Constrains
•	There will be no case in which less than 100 coins will be in the field
•	All given numbers will be valid integers in the range [0, 100]
"""


# import sys
# from io import StringIO
#
# test_input1 = """5
# 1 X 7 9 11
# X 14 46 62 0
# 15 33 21 95 X
# P 14 3 4 18
# 9 20 33 X 0
# left
# right
# right
# up
# up
# right
# """
# test_input2 = """8
# 13 18 9 7 24 41 52 11
# 54 21 19 X 6 4 75 6
# 76 5 7 1 76 27 2 37
# 92 3 25 37 52 X 56 72
# 15 X 1 45 45 X 7 63
# 1 63 P 2 X 43 5 1
# 48 19 35 20 100 27 42 80
# 73 88 78 33 37 52 X 22
# up
# down
# up
# left
# """
# sys.stdin = StringIO(test_input2)


def is_outside(row, column, size):
    return row < 0 or row >= size or column < 0 or column >= size


def move_outside(command, row, column, size):
    if command == "up":
        row = size - 1
    elif command == "down":
        row = 0
    elif command == "left":
        column = size - 1
    elif command == "right":
        column = 0
    return row, column


def player_move(command, player_row, player_column, field):
    player_row, player_column = directions[command](player_row, player_column)
    if is_outside(player_row, player_column, len(field)):
        player_row, player_column = move_outside(command, player_row, player_column, size)
    return player_row, player_column


size = int(input())
field = []
player_row, player_column = None, None
coins = 0
path = []
for row in range(size):
    line = [i if i.isalpha() else int(i) for i in input().split()]  # numbers as int, all letters as string
    field.append(line)
    if "P" in line:
        player_row, player_column = row, line.index("P")
        path.append([player_row, player_column])

directions = {
    "up": lambda row, column: (row - 1, column),
    "down": lambda row, column: (row + 1, column),
    "left": lambda row, column: (row, column - 1),
    "right": lambda row, column: (row, column + 1),
}

while coins < 100:
    command = input()
    if command in directions:
        field[player_row][player_column] = 0
        player_row, player_column = player_move(command, player_row, player_column, field)
        path.append([player_row, player_column])
    if field[player_row][player_column] == "X":
        coins //= 2
        break
    else:
        coins += field[player_row][player_column]
        field[player_row][player_column] = "P"

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
print(*path, sep="\n")
