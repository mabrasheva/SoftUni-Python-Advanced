"""
You will receive a number N. On the following N lines, you will be receiving names.
You should sum the ASCII values of each letter in the name and integer divide it by the number of the current row
(starting from 1). Save the result to a set of either odd or even numbers, depending on if the resulting number is odd
or even. After that, sum the values of each set.
•	If the sums of the two sets are equal, print the union of the values, separated by ", ".
•	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values,
separated by ", ".
•	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values,
separated by ", ".
NOTE: On every operation, the starting set should be the odd set
"""


def sum_of_ascii(name: str, row: int):
    return (sum(ord(char) for char in name)) // row


def sets_calculations(odd: set, even: set):
    if sum(odd) == sum(even):
        result = odd.union(even)
        return ", ".join(str(i) for i in result)
    elif sum(odd) > sum(even):
        result = odd.difference(even)
        return ", ".join(str(i) for i in result)
    elif sum(odd) < sum(even):
        result = odd.symmetric_difference(even)
        return ", ".join(str(i) for i in result)


names_count = int(input())
odd_set = set()
even_set = set()

row = 0
for _ in range(names_count):
    name = input()
    row += 1
    name_ascii_sum = sum_of_ascii(name, row)

    if name_ascii_sum % 2 != 0:
        odd_set.add(name_ascii_sum)
    else:
        even_set.add(name_ascii_sum)

print(sets_calculations(odd_set, even_set))
