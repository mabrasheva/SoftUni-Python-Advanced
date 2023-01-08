"""Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple
numbers (integers) as additional arguments (*args). The function should return the result of the operator applied to all
the numbers. For more clarification, see the examples below.
Submit only your function in the Judge system.
Note: Be careful when you have multiplication and division
"""


def operate(operator, *args):
    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for element in args[1::]:
            result -= element
        return result

    def multiply():
        result = 1
        for element in args:
            result *= element
        return result

    def divide():
        result = args[0]
        for element in args[1::]:
            if element == 0:
                continue
            else:
                result /= element
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
