"""A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked
from A to H. We have a total of 64 squares. Each square is represented by a combination of letters and a number
(a1, b1, c1, etc.). In this problem colors of the board will be ignored.
We will play the game with two pawns, white (w) and black (b), where they can:
•	Only move forward in a straight line:
	White (w) moves from the 1st rank to the 8th rank direction.
	Black (b) moves from 8th rank to the 1st rank direction.
•	Can move only 1 square at a time.
•	Can capture another pawn in from of them only diagonally.
When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st
rank), can be promoted to a queen.
Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white
pawn (w), then black moves (b), then white (w) again, and so on.
Some rules apply when moving paws:
•	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn.
When a pawn captures another pawn, the game is over.
•	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
Input
•	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
o	Empty positions are marked with "-".
o	White pawn is marked with "w"
o	Black pawn is marked with "b"
Output
Print either one of the following:
•	If a pawn captures the other, print:
o	"Game over! {White/Black} win, capture on {square}."
•	If a pawn reaches the last rank, print:
o	"Game over! {White/Black} pawn is promoted to a queen at {square}."
Constraints
•	The input will always be valid.
•	The matrix will always be 8x8.
•	There will be no case where two pawns are placed on the same square.
•	There will be no case where two pawns are placed on the same column.
•	There will be no case where black/white will be placed on the last rank.
"""

import string


# import sys
# from io import StringIO
#
# test_input1 = """- - - - - - b -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -
# """
# test_input2 = """- - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# b - - - - - - -
# - w - - - - - -
# - - - - - - - -
# """
#
# test_input3 = """- - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# b - - w - - - -
# - - - - - - - -
# """
#
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def move(pawn, row, column):
    return [row - 1, column] if pawn == "white" else [row + 1, column]


def winner(pawn, row):
    if pawn == "white" and row == 0:
        return True
    elif pawn == "black" and row == size - 1:
        return True
    return False


def capture(pawn, white_row, white_column, black_row, black_column):
    if pawn == "white":
        if [white_row - 1, white_column - 1] == [black_row, black_column]:
            return True
        elif [white_row - 1, white_column + 1] == [black_row, black_column]:
            return True
    elif pawn == "black":
        if [black_row + 1, black_column - 1] == [white_row, white_column]:
            return True
        elif [black_row + 1, black_column + 1] == [white_row, white_column]:
            return True
    return False


size = 8
pawns = ["white", "black"]
white_row, white_column = None, None
black_row, black_column = None, None
winner_pawn = ""
made_capture = False
matrix = []
for row in range(size):
    line = input().split()
    matrix.append(line)
    for index, element in enumerate(line):
        if element == "w":
            white_row, white_column = row, index
        elif element == "b":
            black_row, black_column = row, index

while True:
    pawn = pawns[0]

    if capture(pawn, white_row, white_column, black_row, black_column):
        winner_pawn = pawn
        made_capture = True
        break

    if pawn == "white":
        white_row, white_column = move(pawn, white_row, white_column)
        if winner(pawn, white_row):
            winner_pawn = pawn
            break
    elif pawn == "black":
        black_row, black_column = move(pawn, black_row, black_column)
        if winner(pawn, black_row):
            winner_pawn = pawn
            break

    pawns[0], pawns[1] = pawns[1], pawns[0]

if made_capture:
    if winner_pawn == "white":
        white_row = black_row
        white_column = black_column
    elif winner_pawn == "black":
        black_row = white_row
        black_column = white_column

column = white_column if winner_pawn == "white" else black_column
column = string.ascii_letters[column]
row = white_row if winner_pawn == "white" else black_row
row = size - row

if not made_capture:
    print(f"Game over! {winner_pawn.capitalize()} pawn is promoted to a queen at {column}{row}.")
else:
    print(f"Game over! {winner_pawn.capitalize()} win, capture on {column}{row}.")
