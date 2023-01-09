# Create a function called kwargs_length() that can receive some keyword arguments and return their length.


def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))

dictionary = {}
print(kwargs_length(**dictionary))
