"""
On the first line, you will receive the starting quantity of water (integer).
Until command "Start" read people names and add them to queue.
Until command "End" read commands:
    - {liters} that the current person in the queue wants to get.
        - if enough quantity of water:
            print "{person_name} got water" and remove him/her from the queue
            remove the liters from the water quantity.
        - if not enough quantity of water:
            print "{person_name} must wait" and remove the person from the queue without reducing the water.
    - refill {liters} - add the given litters to the water quantity
"""

from collections import deque

people = deque()
water_quantity = int(input())
while True:
    command = input()
    if command == "Start":
        break
    else:
        people.append(command)
while True:
    command = input()
    if command == "End":
        print(f"{water_quantity} liters left")
        break
    elif command.startswith("refill "):
        command = command.split()
        liters_to_add = int(command[1])
        water_quantity += liters_to_add
    else:
        liters_wanted = int(command)
        person = people.popleft()
        if liters_wanted <= water_quantity:
            print(f"{person} got water")
            water_quantity -= liters_wanted
        else:
            print(f"{person} must wait")
