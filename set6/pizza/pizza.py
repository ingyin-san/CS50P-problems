"""expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format,
and outputs a table"""

import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if (not sys.argv[1].endswith(".csv")):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            print(tabulate(csv.DictReader(file), headers = "keys", tablefmt = "grid"))
    except (FileNotFoundError):
        sys.exit("File does not exist")
