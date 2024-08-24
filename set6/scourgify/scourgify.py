"""Expects two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name."""

import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if (not sys.argv[1].endswith(".csv")):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[2], 'w') as output_file:
            writer = csv.DictWriter(output_file, fieldnames = ["first", "last", "house"])
            writer.writeheader()

            with open(sys.argv[1]) as input_file:
                for row in csv.DictReader(input_file):
                    writer.writerow({"first": row["name"].split(", ")[1], "last": row["name"].split(", ")[0], "house": row["house"]})
    except (FileNotFoundError):
        sys.exit("File does not exist")
