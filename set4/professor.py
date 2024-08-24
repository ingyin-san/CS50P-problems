"""Prompts the user for a level, n. If not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems. Prompts the user to solve each of those problems.
ultimately output the user’s score: the number of correct answers out of 10."""

import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for _ in range(3):
            try:
                ans = int(input(f"{x} + {y} = ").strip())
                if ans == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")

    print("Score:", score)


def get_level():
    try:
        level = int(input("Level: ").strip())
        if (level in [1, 2, 3]):
            return level
        get_level()
    except ValueError:
        get_level()


def generate_integer(level):
    if (level == 1):
        integer = random.randint(0, 9)
    elif (level == 2):
        integer = random.randint(10, 99)
    elif (level == 3):
        integer = random.randint(100, 999)
    else:
        raise ValueError
    
    return integer


if __name__ == "__main__":
    main()
