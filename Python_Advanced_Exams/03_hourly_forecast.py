"""Patricia wants to go on vacation for the weekend and wants to know where the weather will be the best, so she can see
the most sights. Patricia is busy at work and doesn't have time to think about the perfect place for her vacation, so
she wants your help.
Write a function called forecast that stores information about the weather, and returns sorted information for all
locations. The function will receive a different number of arguments. The arguments will be passed as tuples with two
elements - the first one is the location, and the second one is the weather:
•	Location name: string
o	any string
•	Weather: string
o	"Sunny"
o	"Rainy"
o	"Cloudy"
First, sort all locations by weather. First are positioned the locations with sunny weather, next are the locations with
cloudy weather, and last are the locations with rainy weather. For each sequence of locations (e.g. all sunny
locations), sort them by their name in ascending order (alphabetically).
In the end, return the output as described below.
Input
•	There will be no input from the console, just parameters passed to your function
Output
•	The output should look like this:
"{first_sorted_location} - {weather}"
"{second_sorted_location} - {weather}"
…
"{last_sorted_location} - {weather}"
Constraints
•	Each tuple given will always contain the location with its weather.
•	You will never receive the same location twice or more times.
"""


def forecast(*args):
    result = {}
    for location, weather in args:
        if weather not in result:
            result[weather] = []
        result[weather].append(location)

    result_sorted = {weather: sorted(location) for weather, location in result.items()}

    final_result = []
    if "Sunny" in result_sorted:
        final_result.extend([f"{location} - Sunny" for location in result_sorted["Sunny"]])
    if "Cloudy" in result_sorted:
        final_result.extend([f"{location} - Cloudy" for location in result_sorted["Cloudy"]])
    if "Rainy" in result_sorted:
        final_result.extend([f"{location} - Rainy" for location in result_sorted["Rainy"]])

    return "\n".join(final_result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print()

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
