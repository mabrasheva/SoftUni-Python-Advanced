"""You are given a file called text.txt.
 Create a program that opens the file.
 If the file is found, print 'File found'.
 If the file is not found, print 'File not found'.
"""

try:
    with open("./text.txt") as file:
        print("File found")
except FileNotFoundError:
    print("File not found")
