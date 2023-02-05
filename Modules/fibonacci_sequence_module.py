def create(number):
    if number == 1:
        return [0]
    if number == 2:
        return [0, 1]
    sequence = [0, 1]
    for number in range(2, number):
        sequence.append(sequence[-2] + sequence[-1])
    return " ".join([str(i) for i in sequence])


def locate(number: int, sequence: list):
    if number in sequence:
        return f"The number - {number} is at index {sequence.index(number)}"
    else:
        return f"The number {number} is not in the sequence"
