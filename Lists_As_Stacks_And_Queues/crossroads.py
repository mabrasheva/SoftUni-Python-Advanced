"""
Your job is to keep track of the traffic at the crossroads and report whether a crash happened or everyone passed the
crossroads safely.
Sam is on a single lane of cars that queue until the light goes green. When it does, they start passing one by one on a
flashing green light and during the free window before the intersecting road's light goes green. For each second, only
one part of a car (a single character) passes the crossroad. If a car is still in the middle of the crossroads when the
free window ends, it will get hit at the first character that is still in the crossroads.
Input
•	On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
•	On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
•	On the following lines, until you receive the "END" command, you will receive one of two things:
	A car - a string containing the model of the car, or
	The command "green" that indicates the start of a green light cycle
A green light cycle goes as follows:
•	During the green light, cars will enter and exit the crossroads one by one
•	During the free window, cars will only exit the crossroads
Output
•	If a crash happens, end the program and print:
"A crash happened!"
"{car} was hit at {character_hit}."
•	If everything goes smoothly, and you receive an "END" command, print:
"Everyone is safe."
"{total_cars_passed} total cars passed the crossroads."
"""

from collections import deque

green_light_seconds = int(input())  # 1..100
free_window_seconds = int(input())  # 0..100
crash = False
total_cars_passed = 0
crash_result = ""
cars = deque()

while True:
    command = input()
    if command == "END" or crash:
        break
    if command != "green":
        cars.append(command)
    else:
        green_light_seconds_left = green_light_seconds
        while cars and green_light_seconds_left > 0:
            car = cars.popleft()
            if len(car) <= green_light_seconds_left:
                green_light_seconds_left -= len(car)
                total_cars_passed += 1
            elif len(car) <= green_light_seconds_left + free_window_seconds:
                free_window_seconds -= len(car) + green_light_seconds_left
                green_light_seconds_left = 0
                total_cars_passed += 1
            else:
                crash = True
                characters_passed = green_light_seconds_left + free_window_seconds
                character_hit = car[characters_passed:characters_passed + 1]
                crash_result = f"{car} was hit at {character_hit}."
                break

if not crash:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
else:
    print("A crash happened!")
    print(f"{crash_result}")
