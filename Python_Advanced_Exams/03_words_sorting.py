"""Write a function words_sorting which receives a different number of words.
Create a dictionary, which will have as keys the words that the function received. For each key, create a value that is the sum of all ASCII values of that key.
Then, sort the dictionary:
•	By values in descending order, if the sum of all values of the dictionary is odd
•	By keys in ascending order, if the sum of all values of the dictionary is even
Input
•	There will be no input, just any number of words passed to your function
Output
•	The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
Constraints:
•	There will be no case with capital letters.
•	There will be no case with a string consisting of other than letters.
"""


def words_sorting(*args):
    words = {}
    for word in args:
        words[word] = sum(ord(character) for character in word)
    sum_values = sum(words.values())
    if sum_values % 2 == 1:
        words = {key: value for key, value in sorted(words.items(), key=lambda x: -x[1])}
    else:
        words = {key: value for key, value in sorted(words.items(), key=lambda x: x[0])}
    result = [f"{key} - {value}" for key, value in words.items()]
    return "\n".join(result)


"""
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print()
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print()
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
"""
