"""Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0. Before
you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words."""

symbols = ["-", ",", ".", "!", "?"]

with open("./text.txt") as file:
    for index, line in enumerate(file.readlines()):
        if index % 2 == 0:
            line = line.strip().split()[::-1]
            line = " ".join(line)
            for symbol in symbols:
                line = line.replace(symbol, "@")
            print(line)
