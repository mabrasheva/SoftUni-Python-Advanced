"""
You will have to find all possible color combinations that can be used.
Write a program that finds colors in a string. You will be given a string on a single line containing substrings
(separated by a single space) from which you will be able to form the following colors:
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
To form a color, you should concatenate the first and the last substrings and check if you can get any of the above
colors' names. If there is only one substring left, you should use it to do the same check.
You can only keep a secondary color if the two main colors needed for its creation could be formed from the given
substrings:
•	orange = red + yellow
•	purple = red + blue
•	green = yellow + blue
Note: You could find some of the main colors needed to keep a secondary color after it is found.
When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and
return them in the middle of the original string. If the string contains an odd number of substrings, you should put the
substrings one position ahead.
For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye",
so you should remove the last character and return them in the middle of the string: "r by yellow".
In the end, print out the list with colors in the order in which they are found.
Input
•	Single line string
Output
•	The list with the collected colors
Constrains
•	You will not receive an empty string
•	Please consider only the colors mentioned above
•	There won't be any cases with repeating colors
"""

from collections import deque

expression = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}
all_colors = main_colors.union(secondary_colors.keys())

result = []
while expression:
    first_substring = expression.popleft()
    second_substring = expression.pop() if expression else ""

    for color in all_colors:
        if (first_substring + second_substring == color) or (second_substring + first_substring == color):
            result.append(color)
            break
    else:
        first_substring = first_substring[:-1]
        second_substring = second_substring[:-1]
        if first_substring:
            expression.insert(len(expression) // 2, first_substring)
        if second_substring:
            expression.insert(len(expression) // 2, second_substring)

for result_color in result:
    if result_color in secondary_colors:
        if secondary_colors[result_color].issubset(result):
            continue
        else:
            result.remove(result_color)

print(result)
