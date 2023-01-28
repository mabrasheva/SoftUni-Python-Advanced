"""You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
1	2	3	4	5	6	7
24	D	D	D	D	D	8
23	D	T	T	T	D	9
22	D	T	B	T	D	10
21	D	T	T	T	D	11
20	D	D	D	D	D	12
19	18	17	16	15	14	13

Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player.
The score for each turn is deducted from the player’s total score. The first player who reduces their score to zero or
less wins the game.
You are going to receive the information for every throw on a separate line. The coordinate information of a hit will
be in the format: "({row}, {column})".
•	If a player hits outside the dartboard, he does not score any points.
•	If a player hits a number, it is deducted from his total.
•	If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted from
his total.
•	If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted from
his total.
•	"B" is the bullseye. If a player hits it, he wins the game, and the program ends.
For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are
deducted from his total.
Your job is to find who won the game and with how many turns.
Input
•	The name of the first player and the name of the second player, separated by ", "
•	7 lines – the dartboard (separated by single space)
•	On the next lines - the coordinates in the format: "({row}, {column})"
Output
•	You should print only one line containing the winner and his count of throws:
"{name} won the game with {count_turns} throws!"
Constrains
•	There will always be exactly 7 lines
•	There will always be a winner
•	The points will be in range [1, 24]
•	The coordinates will be in range [0, 100]
"""


# import sys
# from io import StringIO
#
# test_input1 = """Ivan, Peter
# 12 21 18 4 20 7 11
# 9 D D D D D 10
# 15 D T T T D 3
# 2 D T B T D 19
# 17 D T T T D 6
# 22 D D D D D 14
# 5 8 23 13 16 1 24
# (3, 3)
# """
# test_input2 = """George, Hristo
# 17 8 21 6 13 3 24
# 16 D D D D D 14
# 7 D T T T D 15
# 23 D T B T D 2
# 9 D T T T D 22
# 19 D D D D D 10
# 12 18 4 20 5 11 1
# (1, 0)
# (2, 3)
# (0, 0)
# (4, 2)
# (5, 1)
# (3, 1)
# (0, 0)
# (2, 3)
# """
#
# sys.stdin = StringIO(test_input1)


def is_outside(row, column, size):
    return row < 0 or row >= size or column < 0 or column >= size


def corresponding_numbers(row, column, size, matrix):
    return int(matrix[0][column]) + int(matrix[size - 1][column]) + int(matrix[row][0]) + int(matrix[row][size - 1])


players_names = input().split(", ")
players_scores = [501, 501]
players_throws = [0, 0]
size = 7
matrix = [input().split() for row in range(size)]
winner = ""
winner_throws = 0

while not winner:
    player = players_names[0]
    players_throws[0] += 1
    throw = [int(i) for i in input().lstrip("(").rstrip(")").split(", ")]
    row, column = throw
    if not is_outside(row, column, size):
        if not matrix[row][column].isalpha():
            players_scores[0] -= int(matrix[row][column])
        elif matrix[row][column] == "D":
            players_scores[0] -= 2 * corresponding_numbers(row, column, size, matrix)
        elif matrix[row][column] == "T":
            players_scores[0] -= 3 * corresponding_numbers(row, column, size, matrix)
        elif matrix[row][column] == "B":
            winner = player
            winner_throws = players_throws[0]
            break
        if players_scores[0] <= 0:
            winner = player
            winner_throws = players_throws[0]
            break
    players_names[0], players_names[1] = players_names[1], players_names[0]
    players_scores[0], players_scores[1] = players_scores[1], players_scores[0]
    players_throws[0], players_throws[1] = players_throws[1], players_throws[0]

print(f"{winner} won the game with {winner_throws} throws!")
