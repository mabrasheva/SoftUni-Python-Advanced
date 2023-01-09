"""
Create a function called age_assignment() that receives a different number of names and a different number of key-value
pairs. The key will be a single letter (the first letter of each name) and the value - a number (age). Find its first
letter in the key-value pairs for each name and assign the age to the person's name.
Then, sort the names in ascending order (alphabetically) and return the information for each person on a new line in the
format: "{name} is {age} years old."
"""


def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        first_letter = name[0]
        for letter in kwargs:
            if letter == first_letter:
                result.append(f"{name} is {kwargs[letter]} years old.")
    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
