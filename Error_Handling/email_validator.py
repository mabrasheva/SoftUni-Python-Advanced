import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = re.compile(r"(?P<name>\w+)@(?P<domain_name>\w+)\.(?P<domain>\w+)")

while True:

    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    match = re.search(pattern, email)
    possible_domains = ["com", "bg", "org", "net"]

    if match:
        if len(match["name"]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        elif match["domain"] not in possible_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        else:
            print("Email is valid")
