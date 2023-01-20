"""
You are provided with the following code. This code raises many exceptions. Fix it, so it works correctly.
It is given a sequence of numbers, separated by a ", ". Iterate through each number by its index, and if the number is smaller or equal to 5, make a multiplication. If the number is larger than 5 and smaller or equal to 10, divide the result by the number. In the end, print the final result.

numbers_list = int(input()).split(", ")
result = 1

for i in range(numbers_list):
    number = numbers_list[i+1]
    if number <= 5
        result *= number
    elif 5 < number <= 10:
        result /= number

print(total)
"""

numbers_list = [int(i) for i in (input()).split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)
