"""
Write a function called get_info that receives a name, an age, and a town and returns a string in the format:
"This is {name} from {town} and he is {age} years old". Use dictionary unpacking when testing your function.
"""


def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


#
# def get_info(**kwargs):
#     name = kwargs["name"]
#     town = kwargs["town"]
#     age = kwargs["age"]
#     return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
