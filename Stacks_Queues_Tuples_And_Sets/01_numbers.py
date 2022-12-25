"""
First, you will be given two sequences of integers values on different lines.
The values of the sequences are separated by a single space between them.
Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
•	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
•	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
•	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
•	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
•	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True".
Otherwise, print "False".
In the end, print the final sequences, separated by a comma and a space ", ".
The values in each sequence should be sorted in ascending order.
"""

sequence_one = set(map(int, input().split()))
sequence_two = set(map(int, input().split()))
commands_number = int(input())
for _ in range(commands_number):
    command = input().split()
    action = command[0]
    if action == "Add":
        sequence, numbers = command[1], {int(i) for i in command[2::]}
        if sequence == "First":
            sequence_one = sequence_one.union(numbers)
        elif sequence == "Second":
            sequence_two = sequence_two.union(numbers)
    elif action == "Remove":
        sequence, numbers = command[1], {int(i) for i in command[2::]}
        if sequence == "First":
            sequence_one = sequence_one.difference(numbers)
        elif sequence == "Second":
            sequence_two = sequence_two.difference(numbers)
    elif action == "Check":
        check_subset = sequence_one.issubset(sequence_two) or sequence_two.issubset(sequence_one)
        print(check_subset)

print(*sorted(sequence_one), sep=", ")
print(*sorted(sequence_two), sep=", ")
