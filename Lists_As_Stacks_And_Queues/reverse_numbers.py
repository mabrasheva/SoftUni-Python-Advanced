"""read a string with N integers from the console, separated by a single space, and reverse them using a stack.
Print the reversed integers on one line, separated by a single space."""

input_string = input().split()
result = []
while input_string:
    result.append(input_string.pop())
print(*result)
