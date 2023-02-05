"""Write a program that encrypts given words by using the characters: "-|_/\()" to structure the word.
Use the pyfiglet module.
You can read more about it here - https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
Directions
1.	First you need to install the module that we will be using. To install it go to Setting --> Project <your_project_name> --> Project Interpreter --> + --> search for pyfiglet --> install package.
2.	Import the module
3.	Implement the logic. We will be using the figlet_format method
"""

from pyfiglet import figlet_format

print(figlet_format(input()))
