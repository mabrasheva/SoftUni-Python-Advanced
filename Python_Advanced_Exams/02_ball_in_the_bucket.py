"""
You are at the funfair to play different games and test your skills. Now you are playing ball in the bucket game.
You will be given a matrix with 6 rows and 6 columns representing the board. On the board, there will be points
(integers) and buckets marked with the letter "B". Rules of the game:
•	You can throw a ball only 3 times.
•	When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
•	You can hit a bucket only once. If you hit the same bucket again, you do not score any points.
•	If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points.
After the board state, you are going to receive the information for every throw on a separate line.
The coordinates’ information of a hit will be in the format: "({row}, {column})".
Depending on how many points you have collected, you win one of the following:
Football	100 to 199 points
Teddy Bear	200 to 299 points
Lego Construction Set	300 and more points

Your job is to keep track of the scored points and to check if you won a prize.
For more clarifications, see the examples below.
Input
•	6 lines – matrix representing the board (each position separated by a single space)
•	On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"

Output
•	On the first line:
o	If you won a prize, print:
"Good job! You scored {points} points, and you've won {prize}."
o	If you did not win any prize, print the points you need to get at least the first prize:
"Sorry! You need {points} points more to win a prize."
Constraints
•	All of the given points will be integers in the range [1, 30]
•	All the given indexes will be integers in the range [0, 30]
•	There always will be exactly 6 buckets - 1 on each column
"""


# import sys
# from io import StringIO
#
# test_input1 = """10 30 B 4 20 24
# 7 8 27 23 11 19
# 13 3 14 B 17 B
# 12 5 21 22 9 6
# B 26 1 28 29 2
# 25 B 16 15 B 18
# (1, 1)
# (20, 15)
# (4, 0)
# """
# test_input2 = """B 30 14 23 20 24
# 29 8 27 18 11 19
# 13 3 B B 17 6
# 28 5 21 22 9 B
# 10 B 26 12 B 2
# 25 1 16 15 7 4
# (0, 0)
# (2, 2)
# (2, 3)
# """


# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

def read_matrix():
    size = 6
    matrix = []
    buckets_coordinates = []
    for row in range(size):
        line = input().split()
        # revert all numbers to int, except buckets which are string
        for index, element in enumerate(line):
            if element == "B":
                buckets_coordinates.append((row, index))
            elif not element.isalpha():
                line[index] = int(element)
        matrix.append(line)

    return matrix, buckets_coordinates


def read_throw_coordinates():
    throw_coordinates = []
    for _ in range(3):
        throw = input().lstrip("(").rstrip(")").split(", ")
        throw_row, throw_column = [int(i) for i in throw]
        throw_coordinates.append((throw_row, throw_column))
    return throw_coordinates


def sum_points_in_same_column(column: int, matrix: list):
    total_sum = 0
    for row in range(len(matrix)):
        if matrix[row][column] != "B":
            total_sum += matrix[row][column]
    return total_sum


def collect_points(throw_coordinates, buckets_coordinates, matrix):
    points = 0
    for coordinates in throw_coordinates:
        if coordinates in buckets_coordinates:
            points += sum_points_in_same_column(coordinates[1], matrix)
            buckets_coordinates.remove(coordinates)
    return points


def win_price(total_points: int, prices: dict):
    if total_points < 100:
        prize = ""
        return False, prize
    else:
        for prize, price in prices.items():
            min_price, max_price = price
            if min_price <= total_points <= max_price:
                return True, prize


prices = {
    "Football": [100, 199],
    "Teddy Bear": [200, 299],
    "Lego Construction Set": [300, float("inf")],
}
matrix, buckets_coordinates = read_matrix()
throw_coordinates = read_throw_coordinates()
total_points = collect_points(throw_coordinates, buckets_coordinates, matrix)
win, prize = win_price(total_points, prices)

if win:
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
