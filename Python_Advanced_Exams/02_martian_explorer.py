"""Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
You will receive a 6x6 field on separate lines with:
•	One rover - marked with the letter "E"
•	Water deposit (one or many) - marked with the letter "W"
•	Metal deposit (one or many) - marked with the letter "M"
•	Concrete deposit (one or many) - marked with the letter "C"
•	Rock (one or many) - marked with the letter "R"
•	Empty positions will be marked with "-"
After that, you will be given the commands for the rover's movement on one line separated by a comma and a space (", ").
Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step, and it can land on one of the given types of
deposit or a rock:
•	When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and increase
its value by 1.
•	If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below,
and the program ends.
•	If the rover goes out of the field, it should continue from the opposite side in the same direction.
Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at
position (3, 5).
The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
Stop the program if you run out of commands or the rover gets broken.
Input
•	On the first 6 lines, you will receive the matrix.
•	On the following line, you will receive the commands for the rover separated by a comma and a space.
Output
•	For each deposit found while you go through the commands, print out on the console: "{Water, Metal or Concrete}
deposit found at ({row}, {col})"
•	If the rover hits a rock, print the coordinates where it got broken in the format:
"Rover got broken at ({row}, {col})"
After you go through all the commands or the rover gets broken, print out on the console:
•	If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
•	Otherwise, print on the console: "Area not suitable to start the colony."
"""


def is_outside(row, column, size):
    return row < 0 or column < 0 or row >= size or column >= size


size = 6
field = []
rover_row, rover_column = 0, 0
for row in range(size):
    field.append(input().split())
    if "E" in field[row]:
        rover_row = row
        rover_column = field[row].index("E")

commands = input().split(", ")

directions = {
    "up": lambda row, column: (row - 1, column),
    "down": lambda row, column: (row + 1, column),
    "left": lambda row, column: (row, column - 1),
    "right": lambda row, column: (row, column + 1),
}

directions_out = {
    "up": lambda row, column: (size - 1, column),
    "down": lambda row, column: (0, column),
    "left": lambda row, column: (row, size - 1),
    "right": lambda row, column: (row, 0),
}

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

for command in commands:
    rover_row, rover_column = directions[command](rover_row, rover_column)
    if is_outside(rover_row, rover_column, size):
        rover_row, rover_column = directions_out[command](rover_row, rover_column)
    if field[rover_row][rover_column] == "W":
        water_deposit += 1
        print(f"Water deposit found at ({rover_row}, {rover_column})")
    elif field[rover_row][rover_column] == "M":
        metal_deposit += 1
        print(f"Metal deposit found at ({rover_row}, {rover_column})")
    elif field[rover_row][rover_column] == "C":
        concrete_deposit += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_column})")
    elif field[rover_row][rover_column] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_column})")
        break

if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

# for row in field:
#     print(row)
# print(rover_row)
# print(rover_column)
