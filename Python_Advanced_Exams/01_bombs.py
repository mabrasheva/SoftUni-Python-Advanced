"""You will be given two sequences of integers, representing bomb effects and bomb casings.
You need to start from the first bomb effect and try to mix it with the last bomb casing.
If the sum of their values is equal to any of the materials in the table below – create the bomb corresponding to the
value and remove both bomb materials. Otherwise, just decrease the value of the bomb casing by 5. You need to stop
combining when you have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.
Bombs:
•	Datura Bombs: 40
•	Cherry Bombs: 60
•	Smoke Decoy Bombs: 120
To fill the bomb pouch, Ezio needs three of each of the bomb types.
Input
•	On the first line, you will receive the integers representing the bomb effects, separated by ", ".
•	On the second line, you will receive the integers representing the bomb casings, separated by ", ".
Output
•	On the first line, print:
o	if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
o	if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
•	On the second line, print all bomb effects left:
o	If there are no bomb effects: "Bomb Effects: empty"
o	If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
•	On the third line, print all bomb casings left:
o	If there are no bomb casings: "Bomb Casings: empty"
o	If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
•	Then, you need to print all bombs and the count you have of them, ordered alphabetically:
o	"Cherry Bombs: {count}"
o	"Datura Bombs: {count}"
o	"Smoke Decoy Bombs: {count}"
Constraints
•	All the given numbers will be valid integers in the range [0, 120].
•	There will be no cases with negative material.
"""


def bomb_pouch(bombs_count: dict):
    return all([value >= 3 for value in bombs_count.values()])


from collections import deque

effects = deque(list(map(int, input().split(", "))))
casings = list(map(int, input().split(", ")))
bombs_values = {
    "Datura": 40,
    "Cherry": 60,
    "Smoke Decoy": 120,
}
bombs_count = {
    "Datura": 0,
    "Cherry": 0,
    "Smoke Decoy": 0,
}

while effects and casings and not bomb_pouch(bombs_count):
    effect = effects.popleft()
    casing = casings.pop()
    for bomb_name, bomb_value in sorted(bombs_values.items()):
        if bomb_value == effect + casing:
            bombs_count[bomb_name] += 1
            break
    else:
        effects.appendleft(effect)
        casings.append(casing - 5)

if bomb_pouch(bombs_count):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if not effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(i) for i in effects])}")
if not casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(i) for i in casings])}")
for key, value in sorted(bombs_count.items()):
    print(f"{key} Bombs: {value}")
