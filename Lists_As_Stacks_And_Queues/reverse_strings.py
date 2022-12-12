"""Write program that:
•	Reads an input string
•	Reverses it using a stack
•	Prints the result back on the console
"""

input_string = input()
stack = list(input_string)
result = []
while stack:
    result.append(stack.pop())

print(*result, sep="")
