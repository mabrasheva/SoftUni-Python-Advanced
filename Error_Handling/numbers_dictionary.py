"""
There is some missing code in the solution, and some errors may occur.
Complete the code, so the following errors are handled:
•	Passing non-integer type to the variable number
•	Searching for a non-existent number
•	Removing a non-existent number
Print appropriate messages when an error has occurred. The messages should be:
•	"The variable number must be an integer"
•	"Number does not exist in dictionary" - for non-existing keys
"""

numbers_dictionary = {}

line = input()
while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()
while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)
