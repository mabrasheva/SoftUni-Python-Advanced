"""
You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number in
the format "{number} - {count} times". The number must be formatted to the first decimal point.
"""
numbers_list = [float(i) for i in input().split()]
numbers_occurrence = {}
for number in numbers_list:
    if number not in numbers_occurrence:
        numbers_occurrence[number] = 0
    numbers_occurrence[number] += 1

for number, occurrence in numbers_occurrence.items():
    print(f"{number} - {occurrence} times")
