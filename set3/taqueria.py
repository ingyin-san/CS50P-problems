"""enables a user to place an order, prompting them for items, one per line, until the user inputs control-d.
After each inputted item, the total cost of all items inputted thus far are displayed,
prefixed with a dollar sign ($) and formatted to two decimal places"""

dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        item = input("Item: ").title()
        total += dict[item]
        print(f"Total: ${total:.2f}")
    except KeyError:
        pass
    except EOFError:
        print()
        break
