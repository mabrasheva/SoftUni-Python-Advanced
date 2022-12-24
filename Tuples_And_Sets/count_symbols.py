"""
Write a program that reads a text from the console and counts the occurrences of each character in it.
Print the results in alphabetical (lexicographical) order.
"""
text = tuple(input())
result = set()
for character in text:
    result.add(f"{character}: {text.count(character)} time/s")
print(*sorted(result), sep="\n")
