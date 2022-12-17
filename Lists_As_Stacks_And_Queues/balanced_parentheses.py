# determine whether the expression is balanced

parenthesis = input()
opening_parenthesis = []
parenthesis_dict = {
    "{": "}",
    "[": "]",
    "(": ")"
}
balanced = True

for element in parenthesis:
    if element in "{[(":
        opening_parenthesis.append(element)
    else:
        if opening_parenthesis:
            last_opening_bracket = opening_parenthesis.pop()
            if parenthesis_dict[last_opening_bracket] != element:
                balanced = False
                break
        else:
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")
