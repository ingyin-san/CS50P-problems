"""expects exactly one command-line argument, the name (or path) of a Python file, and
outputs the number of lines of code in that file, excluding comments and blank lines"""

import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if (not sys.argv[1].endswith(".py")):
        sys.exit("Not a python file")

    try:
        count = 0
        with open(sys.argv[1]) as file:
            for line in file:
                if (not (line.lstrip().startswith("#") or line.isspace())):
                    count += 1
        print(count)
    except (FileNotFoundError):
        sys.exit("File does not exist")
