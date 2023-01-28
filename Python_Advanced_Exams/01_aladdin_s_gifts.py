"""First, you will receive a sequence of integers representing the materials for every wedding present.
After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.
Gift	Magic needed
Gemstone	100 to 199
Porcelain Sculpture	200 to 299
Gold	300 to 399
Diamond Jewellery	400 to 499
To make a present, you should take the last integer of materials and sum it with the first magic level value.
If the result is between or equal to the numbers described in the table above, you make the corresponding gift and
remove both materials and magic value. Otherwise:
•	If the product of the operation is under 100:
o	And if it is an even number, double the materials, and triple the magic, then sum it again.
o	And if it is an odd number, double the sum of the materials and the magic level. Then, check again if it is between
or equal to any of the numbers in the table above.
•	If the product of the operation is more than 499, divide the sum of the material and the magic level by 2.
Then, check again if it is between or equal to any of the numbers in the table above.
•	If, however, the result is not between or equal to any of the numbers in the table above after performing the
calculation, remove both the materials and the magic level.
Stop crafting gifts when you are out of materials or magic level.
You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a sculpture or
gold and jewellery.
Input
•	The first line of input will represent the values of materials - integers, separated by a single space
•	On the second line, you will be given the magic levels - integers, separated by a single space
Output
•	On the first line - print whether you have succeeded in crafting the presents:
o	"The wedding presents are made!"
o	"Aladdin does not have enough wedding presents."
•	On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
o	"Materials left: {material1}, {material2}, …"
o	"Magic left: {magicValue1}, {magicValue2}, …
•	On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
"{present1}: {amount}
{present2}: {amount}
…
{presentN}: {amount}"
Constraints
•	All the materials values will be integers in the range [1, 1000]
•	Magic level values will be integers in the range [1, 1000]
"""

from collections import deque


def check_if_gift_crafted(total_sum: int, gifts_crafted: dict, gifts_prices: dict):
    for gift, price in gifts_prices.items():
        min_price, max_price = price
        if min_price <= total_sum <= max_price:
            if gift not in gifts_crafted:
                gifts_crafted[gift] = 0
            gifts_crafted[gift] += 1


def craft(materials: list, magic_levels: deque, gifts_crafted: dict, gifts_prices: dict):
    while materials and magic_levels:
        material = materials.pop()
        magic = magic_levels.popleft()
        total_sum = material + magic
        if total_sum > 499:
            total_sum /= 2
            check_if_gift_crafted(total_sum, gifts_crafted, gifts_prices)
        elif 100 <= total_sum <= 499:
            check_if_gift_crafted(total_sum, gifts_crafted, gifts_prices)
        else:
            if total_sum % 2 == 0:
                total_sum = material * 2 + magic * 3
                check_if_gift_crafted(total_sum, gifts_crafted, gifts_prices)
            else:
                total_sum *= 2
                check_if_gift_crafted(total_sum, gifts_crafted, gifts_prices)
    return gifts_crafted


materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
gifts_crafted = {}
gifts_prices = {
    "Diamond Jewellery": [400, 499],
    "Gold": [300, 399],
    "Porcelain Sculpture": [200, 299],
    "Gemstone": [100, 199],
}

gifts_crafted = craft(materials, magic_levels, gifts_crafted, gifts_prices)

succeeded = False
if ("Gemstone" in gifts_crafted and "Porcelain Sculpture" in gifts_crafted) or \
        ("Gold" in gifts_crafted and "Diamond Jewellery" in gifts_crafted):
    succeeded = True

if succeeded:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
for gift, count in sorted(gifts_crafted.items()):
    print(f"{gift}: {count}")
