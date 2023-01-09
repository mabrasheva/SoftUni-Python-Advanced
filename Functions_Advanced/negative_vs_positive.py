"""
You will receive a sequence of numbers (integers) separated by a single space.
Separate the negative numbers from the positive. Find the total sum of the negatives and positives, and print the
following:
•	On the first line, print the sum of the negatives
•	On the second line, print the sum of the positives
•	On the third line:
o	If the absolute negative number is larger than the positive number:
	"The negatives are stronger than the positives"
o	If the positive number is larger than the absolute negative number:
	"The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input.
"""


def sum_numbers(*args):
    sum_positive = 0
    sum_negative = 0
    for number in args:
        if number < 0:
            sum_negative += number
        else:
            sum_positive += number
    print(sum_negative)
    print(sum_positive)
    if abs(sum_negative) > sum_positive:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


text = [int(x) for x in input().split()]
sum_numbers(*text)
