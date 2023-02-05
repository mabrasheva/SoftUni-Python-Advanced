

def mathematical_operations(text: str):
    first, operator, second = text.split()
    first, second = float(first), float(second)

    if operator == "+":
        return f"{(first + second):.2f}"

    if operator == "-":
        return f"{(first - second):.2f}"

    if operator == "/":
        return f"{(first / second):.2f}"

    if operator == "*":
        return f"{(first * second):.2f}"

    if operator == "^":
        return f"{(first ** second):.2f}"