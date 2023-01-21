"""You will be given some emails until you receive the command "End".
Create the following custom exceptions to validate the emails:
· NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in the
email "peter@gmail.com")
· MustContainAtSymbolError - raise it when there is no "@" in the email
· InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
When an error is encountered, raise it with an appropriate message:
· NameTooShortError - "Name must be more than 4 characters"
· MustContainAtSymbolError - "Email must contain @"
· InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
If the current email is valid, print "Email is valid" and read the next one"""

import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = re.compile(r"(?P<name>\w+)@(?P<domain_name>[a-z]+)\.(?P<domain>[a-z]+)")

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

    else:
        continue
