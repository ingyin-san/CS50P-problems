"""a program that prompts the user for an email address via input and then prints Valid or Invalid, respectively,
if the input is a syntatically valid email address"""

from validator_collection import checkers

prompt = input("What's your email address? ").strip()

if checkers.is_email(prompt):
    print("Valid")
else:
    print("Invalid")
