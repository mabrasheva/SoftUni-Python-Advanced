"""
Write a program that keeps all the unique chemical elements.
On the first line, you will be given a number n - the count of input lines that you will receive.
On the following n lines, you will be receiving chemical compounds separated by a single space.
Your task is to print all the unique ones on separate lines (the order does not matter)
"""
number_of_elements = int(input())
elements = set()
for _ in range(number_of_elements):
    elements_to_add = input().split()
    [elements.add(element) for element in elements_to_add]
print(*elements, sep="\n")
