"""
chocolates -> stack
cups_of_milk -> deque
if last chocolate == first cup of milk, you should make a milkshake and remove both ingredients.
else: you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5 without
moving it from its position.
If any of the values are equal to or below 0, you should remove them from the records right before mixing them with the
other ingredient.
Break when you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left.
"""

from collections import deque

chocolates = [int(i) for i in input().split(", ")]
cups_of_milk = deque(int(i) for i in input().split(", "))
milkshakes = 0
while milkshakes < 5 and chocolates and cups_of_milk:

    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if chocolate <= 0 and milk <= 0:
        continue

    elif chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue

    elif milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        cups_of_milk.append(milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")
