"""Create a program that will receive commands until the command "End". The commands can be:
•	"Create-{file_name}" - Creates the given file with an empty content.
If the file already exists, remove the existing text in it (as if the file is created again)
•	"Add-{file_name}-{content}" - Append the content and a new line after it.
If the file does not exist, create it, and add the content
•	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string
with the new string. If the file does not exist, print: "An error occurred"
•	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
"""

from os.path import join, exists
from os import remove


def file_manipulator(command):
    command = command.split("-")
    action, file_name = command[0], command[1]
    if action == "Create":
        with open(join(".", f"{file_name}"), "w") as file:
            pass
    elif action == "Add":
        content = command[2]
        with open(join(".", f"{file_name}"), "a") as file:
            file.write(f"{content}\n")
    elif action == "Replace":
        old_string, new_string = command[2], command[3]
        if not exists(f"{file_name}"):
            print("An error occurred")
        else:
            with open(join(".", f"{file_name}"), "r+") as file:
                text = file.read().replace(old_string, new_string)
                file.seek(0)
                file.flush()
                file.write(text)
    elif action == "Delete":
        if not exists(f"{file_name}"):
            print("An error occurred")
        else:
            remove(file_name)


while True:
    command = input()
    if command == "End":
        break
    file_manipulator(command)
