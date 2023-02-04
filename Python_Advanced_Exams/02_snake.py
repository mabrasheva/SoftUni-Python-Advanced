"""You will be given an integer n for the size of the snake territory with square shape. On the next n lines, you will
receive the rows of the territory. The snake will be placed on a random position, marked with the letter 'S'.
On random positions there will be food, marked with '*'. There might also be a lair on the territory. The lair has two
burrows. They are marked with the letter - 'B'. All of the empty positions will be marked with '-'.
Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
Move commands will be: "up", "down", "left", "right".
If the snake moves to a food, it eats the food and increases the food quantity with one.
If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows disappear.
If the snake goes out of its territory, it loses, can't return back and the program ends. The snake needs at least 10
food quantity to win.
When the snake has gone outside of its territory or has eaten enough food, the game ends.
Input
•	On the first line, you are given the integer n – the size of the square matrix.
•	The next n lines holds the values for every row.
•	On each of the next lines you will get a move command.
Output
•	On the first line:
o	If the snake goes out of its territory, print: "Game over!"
o	If the snake eat enough food, print: "You won! You fed the snake."
•	On the second line print all food eaten: "Food eaten: {food quantity}"
•	In the end print the matrix.
Constraints
•	The size of the square matrix will be between [2…10].
•	There will always be 0 or 2 burrows, marked with - 'B'.
•	The snake position will be marked with 'S'.
•	The snake will always either go outside its territory or eat enough food.
•	There will be no case in which the snake will go through itself.
"""


# import sys
# from io import StringIO
#
# test_input1 = """6
# -----S
# ----B-
# ------
# ------
# --B---
# --*---
# left
# down
# down
# down
# left
# """
# test_input2 = """7
# --***S-
# --*----
# --***--
# ---**--
# ---*---
# ---*---
# ---*---
# left
# left
# left
# down
# down
# right
# right
# down
# left
# down
# """

# sys.stdin = StringIO(test_input1)


def is_inside(row, column, size):
    return 0 <= row < size and 0 <= column < size


size = int(input())
matrix = []
snake_row = None
snake_column = None
food = set()
burrows = set()
food_quantity = 0

for row in range(size):
    line = list(input())
    matrix.append(line)
    for index, element in enumerate(line):
        if element == "S":
            snake_row, snake_column = row, index
        elif element == "*":
            food.add((row, index))
        elif element == "B":
            burrows.add((row, index))

directions = {
    "up": lambda row, column: (row - 1, column),
    "down": lambda row, column: (row + 1, column),
    "left": lambda row, column: (row, column - 1),
    "right": lambda row, column: (row, column + 1),
}


def snake_move(direction, row, column, directions):
    return directions[direction](row, column)


while is_inside(snake_row, snake_column, size) and food_quantity < 10:
    matrix[snake_row][snake_column] = "."
    direction = input()
    snake_row, snake_column = snake_move(direction, snake_row, snake_column, directions)
    if is_inside(snake_row, snake_column, size):
        if matrix[snake_row][snake_column] == "*":
            food_quantity += 1
        elif matrix[snake_row][snake_column] == "B":
            burrows.remove((snake_row, snake_column))
            matrix[snake_row][snake_column] = "."
            snake_row, snake_column = list(burrows)[0]
        matrix[snake_row][snake_column] = "S"

if not is_inside(snake_row, snake_column, size):
    print("Game over!")
if food_quantity >= 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")

for row in matrix:
    print(*row, sep="")
