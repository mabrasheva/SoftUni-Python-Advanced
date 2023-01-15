"""Tom and Jerry decided to play a game together. The game is a maze of which they need to find a way out.
Monitor their moves closely and find out who the winner will be!
First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ".
The order in which they are received determines the order in which they will take turns. The first player starts first.
Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
•	Only one Exit - marked with the "E" letter
•	Trap (one, many, or none) - marked with the "T" letter
•	Wall (one, many, or none) - marked with the "W" letter
•	Empty positions will be marked with "."
In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will be receiving
coordinates for each of the players. They will be taking turns and stepping on different positions on the board until
one of them find the Exit or falls into a Trap. Here are the rules:
•	If a player hits the letter "E", he escapes the maze and wins the game.
o	Print "{player} found the Exit and wins the game!" and end the program.
•	If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
o	Print "{player} is out of the game! The winner is {winner}." and end the program.
•	If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
o	Print "{player} hits a wall and needs to rest."
•	If a player steps on an empty position ".", nothing happens.
•	Both players can step in the same position at the same time.
Input
•	On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
•	On the following 6 lines, you will receive the maze board (elements will be separated by a space)
•	On the following lines, you will be receiving coordinates in the format: "({row}, {column})"
Output
•	You should print the output as described above.
•	The input coordinates will always be valid.
"""

# import sys
from collections import deque

# from io import StringIO
#
# test_input1 = """Tom, Jerry
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .
# (3, 2)
# (1, 3)
# (5, 1)
# (5, 1)
# """
# sys.stdin = StringIO(test_input1)

players = deque(input().split(", "))
size = 6
maze = [input().split() for row in range(size)]
winner = ""
player_to_be_ignored = []
while True:
    coordinates = input().lstrip("(").rstrip(")").split(", ")
    row, column = [int(i) for i in coordinates]

    if players[0] in player_to_be_ignored:
        player_to_be_ignored.remove(players[0])
        players.append(players.popleft())
        continue

    if maze[row][column] == "E":
        winner = players[0]
        print(f"{winner} found the Exit and wins the game!")
        break

    elif maze[row][column] == "T":
        winner = players[1]
        looser = players[0]
        print(f"{looser} is out of the game! The winner is {winner}.")
        break

    elif maze[row][column] == "W":
        player_to_be_ignored.append(players[0])
        print(f"{players[0]} hits a wall and needs to rest.")

    players.append(players.popleft())
