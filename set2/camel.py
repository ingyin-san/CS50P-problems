#prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case

camel = input("camelCase: ")

snake = ""
for c in camel:
    if c.isupper():
        snake += '_' + c.lower()
    else:
        snake += c
print("snake_case: " + snake)
