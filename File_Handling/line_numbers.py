"""Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and
punctuation marks. The result should be written to another text file."""

from os.path import join
from string import punctuation

with open(join(".", "text.txt")) as input_file, open(join(".", "output_file.txt"), "w") as output_file:
    for index, line in enumerate(input_file):
        letters = 0
        punctuation_marks = 0
        for element in line:
            if element.isalpha():
                letters += 1
            elif element in punctuation:
                punctuation_marks += 1
        output_file.write(f"Line {index + 1}: {line.strip()} ({letters})({punctuation_marks})\n")

