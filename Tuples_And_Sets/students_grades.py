"""
Write a program that reads students' names and their grades and adds them to the student record.
On the first line, you will receive the number of students – N.
On the following N lines, you will be receiving a student's name and their grade.
For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in
the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
The order in which we print the result does not matter.
"""


def average_grade(grades: tuple):
    return sum(grades) / len(grades)


number_of_students = int(input())
students_results = {}
for _ in range(number_of_students):
    name, grade = input().split()
    if name not in students_results:
        students_results[name] = ()
    students_results[name] += (float(grade),)
for name, grades in students_results.items():
    average = average_grade(grades)
    grades_formatted = [f"{i:.2f}" for i in grades]
    print(f"{name} -> {' '.join(grades_formatted)} (avg: {average:.2f})")
