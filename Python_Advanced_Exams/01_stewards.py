"""
You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format "{number}{letter}".
You will also be given two more sequences of numbers only.
First, you have to take the first number of the first sequence and the last number of the second sequence.
Next, take the sum of those two numbers and find its ASCII character.
•	Compare each of the two taken numbers and the found character with the seats.
If you find a match, the passenger is seated, and the seat is considered taken. Remove both numbers from their sequences.
•	If there is no equality, the two numbers should be returned at the end of their sequences (first becomes last, last
becomes first).
•	If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep track of all
rotations made.
The program should end under the following circumstances:
•	You have found 3 (three) seat matches
•	You have made a total of 10 rotations
Input
•	On the first line, you will be given a sequence of seats - strings separated by comma and space ", "
•	On the second and the third line, you will be given two more sequences - integers separated by a comma and a
space ", "
Output
When the program ends, print the following on two different lines:
o	Seat matches: {matches separated by comma and space}
o	Rotations count: {total rotations made}
Constraints
•	All integers will be in the range [1, 100]
•	All letters will be in the range [A-Z]
•	You will never run out of numbers in your sequences before the program ends
•	You will never have more than one match at a time
"""
# import sys
from collections import deque

# from io import StringIO
#
# test_input1 = """17K, 20B, 3C, 15D, 31Z, 28F
# 20, 35, 15, 3, 2, 10
# 1, 15, 64, 53, 45, 46
# """
# test_input2 = """25A, 16B, 44T, 49D, 27M, 44F
# 25, 3, 31, 49, 26, 13
# 10, 15, 44, 40
# """
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

seats = input().split(", ")
first_sequence = deque([int(i) for i in input().split(", ")])
second_sequence = deque(int(i) for i in input().split(", "))
seats_matches = 0
seats_taken = []
rotations = 0

while seats_matches < 3 and rotations < 10:
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()
    letter = chr(first_number + second_number)
    rotations += 1
    for seat in seats:
        if str(first_number) + letter == seat or str(second_number) + letter == seat:
            if seat not in seats_taken:
                seats_matches += 1
                seats_taken.append(seat)
            break
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)

print(f"Seat matches: {', '.join(seats_taken)}")
print(f"Rotations count: {rotations}")
