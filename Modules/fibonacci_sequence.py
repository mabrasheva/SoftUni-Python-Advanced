"""Create a module that can create a Fibonacci sequence up to a number (count of numbers in the sequence) and print
them, separating them with a single space. The module should also be able to locate a specific number in the sequence.
You can read more about the Fibonacci sequence here: https://en.wikipedia.org/wiki/Fibonacci_number
You will be receiving commands until the "Stop" command. The commands are:
•	"Create Sequence {count}". Create a series of numbers up to a specific count and print them in the following format:
           "{n1} {n2} … {n}"
•	"Locate {number}"
Check if the sequence contains the number. If it finds the number, it should print:
"The number - {number} is at index {index}"
And if it doesn't find it:
"The number {number} is not in the sequence"
Input
•	You will be receiving commands until the "Stop" command. All inputs will be valid.
Output
•	Print the output of every command in the format described above.
"""

from fibonacci_sequence_module import create, locate

while True:
    command = input()
    if command == "Stop":
        break
    command = command.split()
    action, number = command[0], int(command[-1])
    sequence = []
    if action == "Create":
        sequence = create(number)
        print(create(number))
    elif action == "Locate":
        print(locate(number, sequence))
