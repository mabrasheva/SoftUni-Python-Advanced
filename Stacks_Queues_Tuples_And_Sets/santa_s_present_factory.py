"""
You should take the last box with materials and the first magic level value to craft a toy.
Their multiplication calculates the total magic level.
If the result equals one of the levels described in the table above, you craft the present and remove both materials and
magic value. Otherwise:
•	If the product of the operation is a negative number, you should sum the values together, remove them both from
their positions, and add the result to the materials.
•	If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the magic
value and increase the material value by 15.
•	If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
Stop crafting presents when you run out of boxes of materials or magic level values.
Your task is considered done if you manage to craft either one of the pairs:
•	a doll and a train
•	a teddy bear and a bicycle

materials -> stack
magic -> deque
presents_crafted -> dict
"""

from collections import deque

materials = list(map(int, input().split()))
magics = deque(map(int, input().split()))
presents_crafted = {}
presents_magic = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400,
}

while materials and magics:

    material = materials.pop()
    magic = magics.popleft()

    if material == 0 and magic == 0:
        continue
    elif material == 0:
        magics.appendleft(magic)
        continue
    elif magic == 0:
        materials.append(material)
        continue

    magic_level = material * magic

    if magic_level < 0:
        materials.append(material + magic)
        continue

    for present, magic_needed in presents_magic.items():
        if magic_level == magic_needed:
            if present not in presents_crafted:
                presents_crafted[present] = 0
            presents_crafted[present] += 1
            break
    else:
        materials.append(material + 15)

if ("Doll" in presents_crafted and "Wooden train" in presents_crafted) or \
        ("Teddy bear" in presents_crafted and "Bicycle" in presents_crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(list(map(str, reversed(materials))))}")
if magics:
    print(f"Magic left: {', '.join(list(map(str, magics)))}")

for present, quantity in sorted(presents_crafted.items()):
    if quantity > 0:
        print(f"{present}: {quantity}")
