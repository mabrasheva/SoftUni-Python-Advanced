"""
Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m, separated by a
single space - representing the lengths of two separate sets. On the next n + m lines, you will receive n numbers, which
are the numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that appear
in both and print them on separate lines (the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}
"""
set_one_length, set_two_length = list(map(int, input().split()))
set_one = set()
set_two = set()
for _ in range(set_one_length):
    set_one.add(input())
for _ in range(set_two_length):
    set_two.add(input())
unique_elements = set_one.intersection(set_two)
print("\n".join(unique_elements))
