from collections import deque


def create_item(sum_resources, item_resources, items_created):
    for item, value in item_resources.items():
        if value == sum_resources:
            if item not in items_created:
                items_created[item] = 0
            items_created[item] += 1
            return True
    if sum_resources > item_resources["MedKit"]:
        if "MedKit" not in items_created:
            items_created["MedKit"] = 0
        items_created["MedKit"] += 1
        remaining_resources = sum_resources - item_resources["MedKit"]
        medicaments[-1] += remaining_resources
        return True
    return False


def print_result(textiles, medicaments):
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
    else:
        if not textiles:
            print("Textiles are empty.")
        elif not medicaments:
            print("Medicaments are empty.")

    for item_name, quantity in sorted(items_created.items(), key=lambda x: (-x[1], x[0])):
        print(f"{item_name} - {quantity}")

    if medicaments:
        medicaments = reversed(medicaments)
        print(f"Medicaments left: {', '.join([str(i) for i in medicaments])}")
    if textiles:
        print(f"Textiles left: {', '.join([str(i) for i in textiles])}")


textiles = deque([int(i) for i in input().split()])
medicaments = [int(i) for i in input().split()]

item_resources = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}
items_created = {}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    sum_resources = textile + medicament

    if create_item(sum_resources, item_resources, items_created):
        continue
    else:
        medicaments.append(medicament + 10)

print_result(textiles, medicaments)
