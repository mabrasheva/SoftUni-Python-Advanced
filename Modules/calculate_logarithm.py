"""Write a program that prints the calculated logarithm of any given number
Input
•	On the first line, you will receive the number (an integer)
•	On the second line, you will receive a number, which is the logarithm base.
It can be either a number or the word "natural"
The output should be formatted to the 2nd decimal digit
"""

from math import log

result = None

number = int(input())
logarithm_base = input()
if logarithm_base.isdigit():
    result = log(number, int(logarithm_base))
elif logarithm_base == "natural":
    result = log(number)
else:
    raise ValueError(f"Invalid input for logarithm base: {logarithm_base}")

if result:
    print(f"{result:.2f}")
