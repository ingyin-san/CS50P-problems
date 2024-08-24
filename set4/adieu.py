#prompts the user for names, one per line, until the user inputs control-d, then bid adieu to those names.

import inflect

p = inflect.engine()

names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    pass

print("Adieu, adieu, to", p.join(names))
