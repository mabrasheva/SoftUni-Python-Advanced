"""
Read a string with kids names.
Read n toss (integer).

Hot Potato is a game in which children form a circle and toss a hot potato.
The counting starts with the first kid. Every nth toss, the child holding the potato leaves the game.
When a kid leaves the game, it passes the potato to the next kid.
It continues until there is only one kid left.
"""

from collections import deque

kids = deque(input().split())
n_toss = int(input())

counter = 0
while len(kids) > 1:
    counter += 1
    kid = kids.popleft()
    if counter < n_toss:
        kids.append(kid)
    else:
        print(f"Removed {kid}")
        counter = 0

print(f"Last is {kids.popleft()}")
