"""
Write a function called fill_the_box that receives a different number of arguments representing:
•	the height of a box
•	the length of a box
•	the width of a box
•	n-times a different number of cubes with exact size 1 x 1 x 1
•	a string "Finish"
Your task is to fill the box with the given cubes until the current argument equals "Finish".
Input
•	There will be no input. Just parameters passed to your function.
Output
The function should return a string in the following format:
•	If, at the end, there is free space left in the box, print:
o	"There is free space in the box. You could put {free space in cubes} more cubes."
•	If there is no free space in the box, print:
o	"No more free space! You have {cubes left} more cubes."
"""


def fill_the_box(height, length, width, *args):
    volume = height * width * length
    elements_left = 0
    for element in args:
        if element == "Finish":
            break

        if volume > 0:
            if element <= volume:
                volume -= element
            else:
                elements_left += element - volume
                volume = 0
        else:
            elements_left += element

    if volume:
        return f"There is free space in the box. You could put {volume} more cubes."
    return f"No more free space! You have {elements_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
