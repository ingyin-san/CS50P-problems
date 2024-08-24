"""Prompts the user for a level, n,
randomly generates an integer between 1 and n, inclusive, and
prompts the user to guess that integer"""

import random
import sys


while True:
    try:
        level = int(input("Level: ").strip())
        if level > 0:
            break
    except ValueError:
        pass


randInt = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: ").strip())
        if guess <= 0:
            continue
        elif guess < randInt:
            print("Too small!")
        elif guess > randInt:
            print("Too large!")
        else:
            sys.exit("Just right!")
    except ValueError:
        pass
