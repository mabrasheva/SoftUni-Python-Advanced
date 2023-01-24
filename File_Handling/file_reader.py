"""You are given a file called numbers.txt.
Create a program that reads the numbers from the file. Print on the console the sum of those numbers.
"""

# Scenario 1:
# with open("numbers.txt") as file:
#     print(sum([int(number) for number in file]))

# Scenario 2:
# total_sum = 0
# with open("numbers.txt") as file:
#     for number in file:
#         total_sum += int(number)
# print(total_sum)

# Scenario 3:
with open("numbers.txt") as file:
    print(sum([int(i) for i in file.readlines()]))