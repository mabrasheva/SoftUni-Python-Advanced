"""
Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.
The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
"""


def even_odd(*args):
    command = args[-1]
    numbers = args[0:-1]
    result = []
    parity = 0 if command == "even" else 1
    for number in numbers:
        if number % 2 == parity:
            result.append(number)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
