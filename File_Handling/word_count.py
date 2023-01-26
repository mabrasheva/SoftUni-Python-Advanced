"""Write a program that reads a list of words from the file words.txt and finds how many times each of the words is
contained in another file text.txt. Matching should be case-insensitive.
The results should be written to other text files. Sort the words by frequency in descending order.
"""
from string import punctuation

words_count = {}

with open("words.txt") as file:
    searched_words = file.read().split()
    searched_words = [word.lower() for word in searched_words]
with open("text.txt") as file:
    # read the whole file as string and revert it to lower case
    text = file.read().lower()
    # remove punctuation and new lines characters
    text = text.translate(str.maketrans('', '', punctuation)).strip()
    text = text.split()

for word in searched_words:
    words_count[word] = text.count(word)

with open("word_count_result.txt", "w") as output_file:
    for word, word_count in sorted(words_count.items(), key=lambda x: -x[1]):
        output_file.write(f"{word} - {word_count}\n")
