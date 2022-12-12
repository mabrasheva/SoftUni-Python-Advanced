"""
Until command "End" reads customers' names and adds them to queue.
If command "Paid" print customers queue and empty queue.
If command "End" print customers queue.
"""

from collections import deque

customers_queue = deque()
while True:
    command = input()
    if command == "End":
        print(f"{len(customers_queue)} people remaining.")
        break
    elif command == "Paid":
        while customers_queue:
            print(customers_queue.popleft())
    else:
        customers_queue.append(command)
