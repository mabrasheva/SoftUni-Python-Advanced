"""
cups - deque
bottles - stack
start picking from the last received bottle and start filling from the first entered cup
cup -= bottle
if cup <= 0 -> remove cup
if cup > bottle --> pick bottles until you reduce the cup's integer value to 0 or less.
if bottle >= cup --> remove cup --> wasted water = bottle - cup
If you have managed to fill up all the cups, print the remaining water bottles, from the last entered – to the first.
Otherwise, you must print the remaining cups ordered by the entrance – from the first entered – to the last.
"""

from collections import deque


def cups_and_bottles(cups, bottles):
    wasted_water = 0
    while cups and bottles:
        cup = cups.popleft()
        while cup > 0 and bottles:
            bottle = bottles.pop()
            if bottle >= cup:
                wasted_water += bottle - cup
            cup -= bottle
    if cups:
        cups_left = ' '.join(str(i) for i in cups)
        print(f"Cups: {cups_left}")
    elif bottles:
        bottles_left = ' '.join(str(i) for i in bottles)
        print(f"Bottles: {bottles_left}")
    print(f"Wasted litters of water: {wasted_water}")


cups = [int(i) for i in input().split()]
cups = deque(cups)
bottles = [int(i) for i in input().split()]
cups_and_bottles(cups, bottles)
