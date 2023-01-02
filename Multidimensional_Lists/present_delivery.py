"""The presents are ready, and Santa has to deliver them to the kids.
You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood
with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live.
If the cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is
marked by "V". There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive.
If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid, he
doesn't drop a present. If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes happy and
extra generous to all the kids around him* (meaning all of them will receive presents - it doesn't matter if naughty or
nice). If Santa has been to a house, the cell becomes "-".
Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to
these cells, or if he does, he returns to the cell where the cookie was.
If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
Keep in mind that you should check whether all the nice kids received presents.
Input
•	On the first line, you are given the integer m - the count of presents
•	On the second - integer n - the size of the neighborhood
•	The following n lines hold the values for every row
•	On each of the following lines you will get a command
Output
•	On the first line:
o	If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
•	Next, print the matrix.
•	In the end, print one of these messages:
o	If he manages to give all the nice kids presents, print:
"Good job, Santa! {count_nice_kids} happy nice kid/s."
o	Otherwise, print:
"No presents for {count nice kids} nice kid/s."
Constraints
•	The size of the square matrix will be between [2…10].
•	Santa's position will be marked with 'S'.
•	There will always be at least 1 nice kid.
•	There won't be a case where the cookie is on the border of the matrix.
"""


def find_santa(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == "S":
                return row, column


def count_nice_kids(matrix):
    nice_kids_count = 0
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == "V":
                nice_kids_count += 1
    return nice_kids_count


def move(row, column, direction):
    if direction == "up":
        return row - 1, column
    elif direction == "down":
        return row + 1, column
    elif direction == "right":
        return row, column + 1
    elif direction == "left":
        return row, column - 1


def valid_coordinates(row, column, size):
    return 0 <= row < size and 0 <= column < size


def get_around_cells(row, column, matrix):
    around_cells = []
    possible_cells = [
        [row - 1, column],
        [row + 1, column],
        [row, column + 1],
        [row, column - 1],
    ]
    for child_row, child_column in possible_cells:
        if valid_coordinates(child_row, child_column, len(matrix)):
            around_cells.append([child_row, child_column])
    return around_cells


def check_house(santa_row, santa_column, matrix, presents, happy_nice_kids):
    if matrix[santa_row][santa_column] == "V":
        presents -= 1
        happy_nice_kids += 1
    elif matrix[santa_row][santa_column] == "C":
        around_cells = get_around_cells(santa_row, santa_column, matrix)
        for row, column in around_cells:
            if matrix[row][column] == "V":
                happy_nice_kids += 1
                presents -= 1
            elif matrix[row][column] == "X":
                presents -= 1
            matrix[row][column] = "-"
    matrix[santa_row][santa_column] = "S"
    return presents, happy_nice_kids


presents_count = int(input())
size_matrix = int(input())

matrix = [list(input().split()) for row in range(size_matrix)]
santa_row, santa_column = find_santa(matrix)
nice_kids_count = count_nice_kids(matrix)
happy_nice_kids = 0

while presents_count:
    command = input()
    if command == "Christmas morning":
        break
    matrix[santa_row][santa_column] = "-"
    santa_row, santa_column = move(santa_row, santa_column, command)
    presents_count, happy_nice_kids = check_house(santa_row, santa_column, matrix, presents_count, happy_nice_kids)

if presents_count == 0 and happy_nice_kids != nice_kids_count:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)
if nice_kids_count == happy_nice_kids:
    print(f"Good job, Santa! {happy_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count - happy_nice_kids} nice kid/s.")
