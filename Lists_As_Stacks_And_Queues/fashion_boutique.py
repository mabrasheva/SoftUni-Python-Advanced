"""
stack clothes sequence of integers
sum clothes values while remove them from the stack
•	If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes (if there
are any left in the box).
•	If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack. Take a new rack
and then hang it up.
In the end, print how many racks you have used to hang up the clothes.
"""

clothes = list(map(int, input().split()))
rack_capacity = int(input())
current_rack_capacity = rack_capacity
racks = 0

sum_clothes = 0
while clothes:
    if racks == 0:
        racks += 1
    if current_rack_capacity >= clothes[-1]:
        current_rack_capacity -= clothes.pop()
    else:
        current_rack_capacity = rack_capacity
        racks += 1

print(racks)
