"""prompts consumers users to input a fruit (case-insensitively) and then
outputs the number of calories in one portion of that fruit"""

dictionary = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cataloupe': 50,
    'grapefruit': 60,
    'grapes': 90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'plums': 70,
    'strawberries': 50,
    'sweet cherries': 100,
    'tangerine': 50,
    'watermelon': 80
}

fruit = input("Item: ").lower()

if fruit in dictionary:
    print("Calories:", dictionary[fruit])
