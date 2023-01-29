"""Create a function called get_magic_triangle which will receive a single parameter (integer n) and it should create a
magic triangle which follows those rules:
•	We start with this simple triangle [[1], [1, 1]]
•	We generate the next rows until we reach n amount of rows
•	Each number in each row is equal to the sum of the two numbers right above it in the triangle
•	If the current number has no neighbor to the upper left/rigth, we just take the existing neighbor
After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5
Input
•	There will be no inputs
•	The function will be tested by passing different values of n
•	You can test your function with the test code below
Constraints
•	N will be in range [2, 100]
"""


def get_magic_triangle(size):
    matrix = []
    for i in range(size + 1):
        row = []
        C = 1
        for j in range(1, i + 1):
            row.append(C)
            C = C * (i - j) // j
        matrix.append(row)
    return matrix[1::]


get_magic_triangle(5)
