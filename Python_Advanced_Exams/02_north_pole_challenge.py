"""You are visiting Santa Claus' workshop, and it is complete chaos. You will need to help Santa find all items
scattered around the workshop.
You will be given the size of the matrix in the format "{rows}, {columns}". It is the Santa's workshop represented as
some symbols separated by a single space:
•	Your position is marked with the symbol "Y"
•	Christmas decorations are marked with the symbol "D"
•	Gifts are marked with the symbol "G"
•	Cookies are marked with the symbol "C"
•	All of the empty positions will be marked with "."
After the field state, you will be given commands until you receive the command "End". The commands will be in the
format "right/left/up/down-{steps}". You should move in the given direction with the given steps and collect all the
items that come across. If you go out of the field, you should continue to traverse the field from the opposite side in
the same direction. You should mark your path with "x". Your current position should always be marked with "Y".
Keep track of all collected items. If you've collected all items at any point, end the program and print: "Merry
Christmas!".
Input
•	On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
•	On the next lines, you will receive each row with its columns - symbols, separated by a single space.
•	On the following lines, you will receive commands in the format described above until you receive the command "End"
 or until you collect all items.
Output
•	On the first line, if you have collected all items, print:
o	"Merry Christmas!"
o	Otherwise, skip the line
•	Next, print the number of collected items in the format:
o	"You've collected:
o	- {number_of_decoration} Christmas decorations
o	- {number_of_gifts} Gifts
o	- {number_of_cookies} Cookies"
•	Finally, print the field, as shown in the examples.
Constrains
•	All the commands will be valid
•	There will always be at least one item
•	The dimensions of the matrix will be integers in the range [1, 20]
•	The field will always have only one "Y"
•	On the field, there will always be only the symbols shown above.
"""


# import sys
# from io import StringIO
#
# test_input1 = """6, 5
# . . . . .
# C . . G .
# . C . . .
# G . . C .
# . D . . D
# Y . . . G
# left-3
# up-1
# left-2
# right-7
# up-1
# End
# """
#
# test_input2 = """5, 6
# . . . . . .
# . . . . . .
# Y C D D . .
# . . . C . .
# . . . C . .
# right-3
# down-3
# """
#
# test_input3 = """5, 2
# . .
# . .
# . Y
# . .
# . G
# up-1
# left-11
# down-10
# End
# """
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def is_outside(row, column, rows, columns):
    return row < 0 or column < 0 or row >= rows or column >= columns


rows, columns = [int(i) for i in input().split(", ")]
matrix = []
player_row, player_column = 0, 0
items = 0
for row in range(rows):
    line = input().split()
    matrix.append(line)
    if "Y" in line:
        player_row = row
        player_column = line.index("Y")
    if "D" in line or "G" in line or "C" in line:
        items += line.count("D") + line.count("G") + line.count("C")

decorations = 0
gifts = 0
cookies = 0

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1)
}
directions_outside = {
    "up": lambda r, c: (rows - 1, c),
    "down": lambda r, c: (0, c),
    "right": lambda r, c: (r, 0),
    "left": lambda r, c: (r, columns - 1)
}

while items > 0:
    command = input()
    if command == "End":
        break
    command = command.split("-")

    direction, steps = command[0], int(command[1])

    for step in range(steps):
        if items == 0:
            break
        matrix[player_row][player_column] = "x"
        player_row, player_column = directions[direction](player_row, player_column)
        if is_outside(player_row, player_column, rows, columns):
            player_row, player_column = directions_outside[direction](player_row, player_column)
        if matrix[player_row][player_column] == "D":
            decorations += 1
            items -= 1
        elif matrix[player_row][player_column] == "G":
            gifts += 1
            items -= 1
        elif matrix[player_row][player_column] == "C":
            cookies += 1
            items -= 1
        matrix[player_row][player_column] = "x"
    matrix[player_row][player_column] = "Y"

    # for row in matrix:
    #     print(*row, sep=" ")
    # print()

if items == 0:
    print("Merry Christmas!")

print(f"""You've collected:
- {decorations} Christmas decorations
- {gifts} Gifts
- {cookies} Cookies""")

for row in matrix:
    print(*row, sep=" ")
