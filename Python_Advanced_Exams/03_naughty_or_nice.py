"""Santa Claus is always watching and seeing if children are good or bad. Only the nice children get Christmas presents,
so Santa Claus is preparing his list this year to check which child has been good or bad.
Write a function called naughty_or_nice_list which will receive
•	A list representing Santa Claus' "Naughty or Nice" list full of kids' names
•	A different number of arguments (strings) and/or keywords representing commands
The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
The list holds a different number of kids - tuples containing two elements: a counting number (integer) at the first
position and a name (string) at the second position.
For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
Next, the function could receive arguments and/or keywords.
Each argument is a command. The commands could be the following:
•	"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number, MOVE the kid to a
list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the command.
•	"{counting_number}-Nice" - if there is only one tuple in the given list with the same number, MOVE the kid to a list
with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"):
•	If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE kids
depending on the value in the keyword. Then, remove it from the Santa list.
•	Otherwise, ignore the command.
All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
In the end, return the final lists, each on a new line as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input. Just parameters passed to your function.
Output
•	The function should return strings with the names on each list on separate lines, if there are any, otherwise skip
the line:
o	"Nice: {name1}, {name2} … {nameN}"
o	"Naughty: {name1}, {name2} … {nameN}"
o	"Not found: {name1}, {name2} … {nameN}"
"""


def naughty_or_nice_list(kids_list, *args, **kwargs):
    kids = {
        "Nice": [],
        "Naughty": [],
        "Not found": [],
    }

    kids_by_number = {}
    for number, name in kids_list:
        if number not in kids_by_number:
            kids_by_number[number] = []
        kids_by_number[number].append(name)

    for command in args:
        command = command.split("-")
        counting_number = int(command[0])
        naughty_or_nice = command[1]
        if counting_number in kids_by_number:
            if naughty_or_nice == "Naughty" and len(kids_by_number[counting_number]) == 1:
                kids["Naughty"].extend(kids_by_number[counting_number])
                del kids_by_number[counting_number]
            elif naughty_or_nice == "Nice" and len(kids_by_number[counting_number]) == 1:
                kids["Nice"].extend(kids_by_number[counting_number])
                del kids_by_number[counting_number]

    if kwargs:
        for name, word in kwargs.items():
            count = 0
            for number, values in kids_by_number.items():
                if name in values:
                    key = number
                    count += 1
            if count == 1:
                kids[word].append(name)
                for number, values in kids_by_number.items():
                    if name in values:
                        values.remove(name)

    for value in kids_by_number.values():
        if value:
            kids["Not found"].extend(value)

    result = []
    for key, value in kids.items():
        if value:
            result.append(f"{key}: " + ', '.join([str(x) for x in value]))

    return "\n".join(result)


# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))
# print()
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))
print()
# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
