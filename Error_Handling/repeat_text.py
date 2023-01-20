"""Write a program that receives a text on the first line and times (to repeat the text) that must be an integer.
If the user passes a non-integer type for the times variable, handle the exception and print a message
"Variable times must be an integer".
"""

try:
    text = input()
    times = int(input())
    print(text * times)
except ValueError:
    print("Variable times must be an integer")
