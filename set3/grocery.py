"""prompts the user for items, one per line, until the user inputs control-d
Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item."""

grocery_list = {}

while True:
    try:
        item = input().strip().upper()
        if item not in grocery_list:
            grocery_list[item] = 1
        else:
            grocery_list[item] += 1
    except KeyError:
        pass
    except EOFError:
        for grocery in sorted(grocery_list):
            print(grocery_list[grocery], grocery)
        break
