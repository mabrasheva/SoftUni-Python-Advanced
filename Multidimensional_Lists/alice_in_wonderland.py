"""
Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
You will be given an integer n for the size of the Wonderland territory with a square shape.
On the following n lines, you will receive the rows of the territory:
•	Alice will be placed in a random position, marked with the letter "A".
•	On the territory, there will be bags of tea, represented as numbers.
If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
•	There will always be one rabbit hole on the territory marked with the letter "R".
•	All the empty positions will be marked with ".".
After the field state, you will be given commands for Alice's movements.
Move commands can be: "up", "down", "left" or "right".
When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue
collecting.
Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
In the end, the path she walked had to be marked with '*'.
For more clarifications, see the examples below.
Input
•	On the first line, you will be given the integer n – the size of the square matrix
•	On the following n lines - matrix representing the field (each position separated by a single space)
•	On each of the following lines, you will be given a move command
Output
•	On the first line:
o	If Alice steps on the rabbit hole or she go out of the territory, print:
"Alice didn't make it to the tea party."
o	If she collected at least 10 bags of tea, print:
"She did it! She went to the party."
•	On the following lines, print the matrix.
Constraints
•	Alice will always either go outside the Wonderland or collect 10 bags of tea
•	All the commands will be valid
•	All the given numbers will be valid integers in the range [0, 10]
"""


def find_alice(size):
    for row in range(size):
        for column in range(size):
            if matrix[row][column] == "A":
                return row, column


def valid_coordinates(row, column, size):
    return 0 <= row < size and 0 <= column < size


size_matrix = int(input())
matrix = [[i for i in input().split()] for row in range(size_matrix)]

directions = {
    "up": lambda row, column: (row - 1, column),
    "down": lambda row, column: (row + 1, column),
    "left": lambda row, column: (row, column - 1),
    "right": lambda row, column: (row, column + 1),
}
tea = 0
alice_row, alice_column = find_alice(size_matrix)
while tea < 10:
    matrix[alice_row][alice_column] = "*"
    command = input()
    alice_row, alice_column = directions[command](alice_row, alice_column)

    if not valid_coordinates(alice_row, alice_column, size_matrix):
        break
    elif matrix[alice_row][alice_column] == "R":
        matrix[alice_row][alice_column] = "*"
        break
    elif matrix[alice_row][alice_column] == "." or matrix[alice_row][alice_column] == "*":
        matrix[alice_row][alice_column] = "*"
        continue
    else:
        tea += int(matrix[alice_row][alice_column])
        matrix[alice_row][alice_column] = "*"

if tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(*row)
