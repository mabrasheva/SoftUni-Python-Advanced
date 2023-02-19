def is_outside(row, column, row_count, column_count):
    return row < 0 or row >= row_count or column < 0 or column >= column_count


def next_position(direction, row, column, directions):
    return directions[direction](row, column)


rows_count, columns_count = [int(i) for i in input().split()]

ground = []
player_row, player_column = None, None
obstacles = set()
other_players = set()
touched_opponents = 0

for row in range(rows_count):
    line = input().split()
    ground.append(line)
    for index, character in enumerate(line):
        if character == "B":
            player_row = row
            player_column = index
        elif character == "O":
            obstacles.add((row, index))
        elif character == "P":
            other_players.add((row, index))

directions = {
    "up": lambda row, column: (row - 1, column),
    "down": lambda row, column: (row + 1, column),
    "right": lambda row, column: (row, column + 1),
    "left": lambda row, column: (row, column - 1),
}

moves = 0
while other_players:
    command = input()
    if command == "Finish":
        break

    next_row, next_column = next_position(command, player_row, player_column, directions)
    if is_outside(next_row, next_column, rows_count, columns_count):
        continue
    elif (next_row, next_column) in obstacles:
        continue

    if (next_row, next_column) in other_players:
        other_players.remove((next_row, next_column))
        touched_opponents += 1
        ground[next_row][next_column] = "-"

    ground[player_row][player_column] = "-"
    player_row, player_column = next_row, next_column

    moves += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")
