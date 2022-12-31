"""You are going to create a game called "Miner".
First, you will receive the size of a square field in which the miner should move.
On the second line, you will receive the commands for the miner's movement, separated by a single space.
The possible commands are "left", "right", "up" and "down".
In the end, you will receive each row of the field on a separate line.
The possible characters that may appear on the screen are:
•	* - a regular position on the field
•	e - the end of the route
•	c - coal
•	s - miner
The miner starts moving from the position "s". He should perform the given commands successively, moving with only one
position in the given direction. If the miner has reached the edge of the field and the following command indicates that
he has to get out of the area, he must remain in his current position and ignore the command.
When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal.
In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
•	If the miner has collected all coal in the field, the program stops, and you should print the message:
"You collected all coal! ({row_index}, {col_index})".
•	If the miner steps at "e", the game is over (the program stops), and you should print the message:
"Game over! ({row_index}, {col_index})".
•	If there are no more commands and none of the above cases had happened, you should print the message:
"{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
Input
•	Field size - an integer number
•	Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
•	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
Output
•	There are three types of output as mentioned above.
Constraints
•	The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
•	The field will always have only one "s"
"""

from collections import deque


def miner_coordinates(size):
    miner_position = ()
    for row in range(size):
        for column in range(size):
            if matrix[row][column] == "s":
                miner_position = (row, column)
                break
    return miner_position


def coals(size):
    coals_number = 0
    for row in range(size):
        for column in range(size):
            if matrix[row][column] == "c":
                coals_number += 1
    return coals_number


def outside_matrix(row, column, size):
    return row < 0 or column < 0 or row >= size or column >= size


def move(miner_position: tuple, direction: str):
    new_miner_position = miner_position
    miner_row, miner_column = miner_position
    new_miner_row, new_miner_column = new_miner_position
    if direction == "left":
        new_miner_column -= 1
    elif direction == "right":
        new_miner_column += 1
    elif direction == "up":
        new_miner_row -= 1
    elif direction == "down":
        new_miner_row += 1
    if not outside_matrix(new_miner_row, new_miner_column, len(matrix)):
        return new_miner_row, new_miner_column
    else:
        return miner_row, miner_column


square_matrix_size = int(input())
commands = deque(input().split())
matrix = [[i for i in input().split()] for row in range(square_matrix_size)]
game_over = False
collected_all_coal = False
coals_number = coals(square_matrix_size)

while commands and not game_over and not collected_all_coal:

    miner_position = miner_coordinates(square_matrix_size)
    row, column = miner_position
    direction = commands.popleft()
    new_row, new_column = move(miner_position, direction)
    if (new_row, new_column) != miner_position:
        if matrix[new_row][new_column] == "e":
            game_over = True
        elif matrix[new_row][new_column] == "c":
            coals_number -= 1
            if coals_number == 0:
                collected_all_coal = True
        matrix[row][column] = "*"
        matrix[new_row][new_column] = "s"

if game_over:
    print("Game over!", end=" ")
elif collected_all_coal:
    print("You collected all coal!", end=" ")
else:
    print(f"{coals_number} pieces of coal left.", end=" ")
print(miner_coordinates(square_matrix_size))
