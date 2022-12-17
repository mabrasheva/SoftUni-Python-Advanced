"""
Circle road with N petrol pumps
For each petrol pump info:
- The amount of petrol the petrol pump will give you
- The distance from that petrol pump to the next petrol pump (kilometers)
The truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity.
In the beginning, the tank is empty.
Calculate the first petrol pump from where the truck will be able to complete the circle.
You never miss filling its tank at a petrol pump.
Output:
- An integer which will be the smallest index of a petrol pump from which you can start the tour
"""

from collections import deque

pumps_number = int(input())
pumps = deque()
for _ in range(pumps_number):
    pump = input().split()
    pumps.append([int(p) for p in pump])

for index in range(pumps_number):
    current_fuel = 0
    failed = False
    for petrol, distance in pumps:
        current_fuel += petrol
        if current_fuel < distance:
            failed = True
            break
        current_fuel -= distance
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(index)
        break
