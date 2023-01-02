"""
You are participating in a Firearm course. It is a training day at the shooting range.
You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a
single space:
•	Your position is marked with the symbol "A"
•	Targets marked with symbol "x"
•	All of the empty positions will be marked with "."
After the field state, you will be given an integer representing the number of commands you will receive.
The possible commands are:
•	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
You can only move if the field you want to step on is marked with ".".
•	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot
only the nearest target. When you have shot a target, the field becomes empty position (".").
Validate the positions since they can be outside the field.
Keep track of all the shot targets:
•	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets}
targets hit.".
•	If, after you perform all the commands, there are some targets left print:
"Training not completed! {count_left_targets} targets left.".
Finally, print the index positions of the targets that you hit, as shown in the examples.
Input
•	5 lines representing the field (symbols, separated by a single space)
•	N - count of commands
•	On the following N lines - the commands in the format described above
Output
•	On the first line, print one of the following:
o	If all the targets were shot
"Training completed! All {count_targets} targets hit."
o	Otherwise:
"Training not completed! {count_left_targets} targets left."
•	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
Constrains
•	All the commands will be valid
•	There will always be at least one target
"""
import sys
from io import StringIO


def valid_coordinates(row, column, size):
    return 0 <= row < size and 0 <= column < size


size_matrix = 5

player_row = 0
player_column = 0
current_targets_count = 0
hit_targets_count = 0
hit_targets_coordinates = []

matrix = []
for row in range(size_matrix):
    elements = input().split()
    for column in range(size_matrix):
        if elements[column] == "A":
            player_row = row
            player_column = column
        elif elements[column] == "x":
            current_targets_count += 1
    matrix.append(elements)

move = {
    "right": lambda row, column, step: (row, column + step),
    "left": lambda row, column, step: (row, column - step),
    "up": lambda row, column, step: (row - step, column),
    "down": lambda row, column, step: (row + step, column),
}
shoot = {
    "right": lambda row, column: (row, column + 1),
    "left": lambda row, column: (row, column - 1),
    "up": lambda row, column: (row - 1, column),
    "down": lambda row, column: (row + 1, column),
}

commands_count = int(input())
for _ in range(commands_count):

    if current_targets_count == 0:
        break

    command = input().split()
    action, direction = command[0], command[1]

    if action == "move":
        steps = int(command[2])
        new_player_row, new_player_column = move[direction](player_row, player_column, steps)
        if valid_coordinates(new_player_row, new_player_column, size_matrix):
            if matrix[new_player_row][new_player_column] == ".":
                matrix[player_row][player_column] = "."
                matrix[new_player_row][new_player_column] = "A"
                player_row, player_column = new_player_row, new_player_column

    elif action == "shoot":
        target_row, target_column = player_row, player_column
        while True:
            target_row, target_column = shoot[direction](target_row, target_column)
            if valid_coordinates(target_row, target_column, size_matrix):
                if matrix[target_row][target_column] == "x":
                    matrix[target_row][target_column] = "."
                    hit_targets_count += 1
                    current_targets_count -= 1
                    hit_targets_coordinates.append([target_row, target_column])
                    break
            else:
                break

if current_targets_count > 0:
    print(f"Training not completed! {current_targets_count} targets left.")
else:
    print(f"Training completed! All {hit_targets_count} targets hit.")

print(*hit_targets_coordinates, sep="\n")
