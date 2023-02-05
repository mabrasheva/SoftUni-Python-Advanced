def print_triangle(size):
    for row in range(1, size + 2):
        for number in range(1, row):
            print(number, end=" ")
        if row > 1:
            print()
    for row in range(size, 0, -1):
        for number in range(1, row):
            print(number, end=" ")
        if row > 2:
            print()
