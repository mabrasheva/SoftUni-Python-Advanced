"""
You will receive an integer – N. On the next N lines, you will receive queries. Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"
"""

n_number = int(input())
stack = []
for query in range(n_number):
    line = input()
    if line.startswith("1 "):
        line = line.split()
        number_to_push = int(line[1])
        stack.append(number_to_push)
    elif line == "2":
        if stack:
            stack.pop()
    elif line == "3":
        if stack:
            print(max(stack))
    elif line == "4":
        if stack:
            print(min(stack))

result = []
while stack:
    result.append(stack.pop())

print(*result, sep=", ")
