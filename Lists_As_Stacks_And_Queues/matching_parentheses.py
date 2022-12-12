"""You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
Print the result back on the console.
Example: 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
"""
expression = input()
stack = []
result = []
for index, character in enumerate(expression):
    if character == "(":
        stack.append(index)
    elif character == ")":
        start_index = stack.pop()
        end_index = index + 1
        result.append(f"{expression[start_index:end_index]}")

print(*result, sep="\n")
