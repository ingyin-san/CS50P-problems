"""prompts the user for their date of birth in YYYY-MM-DD format and then
sings prints how old they are in minutes, rounded to the nearest integer,
using English words instead of numerals"""

from datetime import date
import operator
import sys
import inflect
import re


def main():
    try:
        dob = input("Date of Birth: ").strip()
        print(convert(date.today(), dob))
    except ValueError:
        sys.exit("Invalid date")


def convert(today, dob):
    matches = re.search(r"^\d{4}-\d{2}-\d{2}$", dob)
    if matches:
        year, month, day = dob.split("-")
        diff = operator.__sub__(today, date(int(year), int(month), int(day)))
        mins = diff.days*24*60

        p = inflect.engine()
        return p.number_to_words(mins).replace(" and", "").capitalize() + " minutes"
    else:
        raise ValueError("Invalid date")


if __name__ == "__main__":
    main()
