"""
Write a program that finds the longest intersection. You will be given a number N.
On each of the next N lines you will be given two ranges in the format:
"{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges.
The start and end numbers in the ranges are inclusive.
Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its
length in the format:
"Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
"""

number_of_ranges = int(input())
longest_intersection = {}
for _ in range(number_of_ranges):
    range_one, range_two = input().split("-")
    range_one = range_one.split(",")
    range_two = range_two.split(",")
    range_one_start, range_one_end = int(range_one[0]), int(range_one[1]) + 1
    range_two_start, range_two_end = int(range_two[0]), int(range_two[1]) + 1
    range_one = set(range(range_one_start, range_one_end))
    range_two = set(range(range_two_start, range_two_end))
    intersection = range_one.intersection(range_two)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
print(f"Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}")
