"""
Write a program to flatten several lists of numbers received in the following format:
	String with numbers or empty strings separated by "|"
	Values are separated by spaces (" ", one or several)
	Order the output list from the last to the first matrix sub-lists and their values from left to right.
"""

lists = input().split("|")
for sublist in lists[::-1]:
    for element in sublist.split():
        print(element.strip(), end=" ")
