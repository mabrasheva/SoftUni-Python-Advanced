"""
quantity of food
sequence of integers representing the quantity of food in each order. Keep the orders in a queue.
Find the biggest order and print it. Next, you will begin servicing your clients from the first one that came. Before each order, check if you have enough food left to complete it:
•	If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
•	Otherwise, stop serving.
"""

from collections import deque

quantity_food = int(input())
sequence = deque(int(i) for i in input().split())
biggest_order = max(sequence)

while sequence and quantity_food >= sequence[0]:
    quantity_food -= sequence.popleft()

print(biggest_order)
if not sequence:
    print("Orders complete")
else:
    orders_left = [str(i) for i in sequence]
    print(f"Orders left: {' '.join(orders_left)}")
