"""Create a function named flights that receives a different number of arguments representing the information about
the flights for a day:
•	the destination of each flight
•	the count of passengers that are boarding the plane
•	a string "Finish"
You need to take each argument and make a dictionary with the plane’s destination as a key and the passengers as a
value of the corresponding key.
If there are more than one flight to the same destination, you should count all the passengers that flew to the
destination.
You should modify the dictionary until the current argument is equal to "Finish".
Input
•	There will be no input, just parameters passed to your function
Output
•	The function should return the final dictionary
Constrains
•	All numbers will be valid integers in the range [0, 300]
•	There will be no flight without given number of passengers
"""


def flights(*args):
    flights_result = {}
    city = ""
    for index, arg in enumerate(args):
        if arg == "Finish":
            break
        if index % 2 == 0:
            city = arg
            if city not in flights_result:
                flights_result[city] = 0
        else:
            passengers = arg
            flights_result[city] += passengers
    return flights_result


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(60 * "-")
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(60 * "-")
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
