"""a function called validate that expects an IPv4 address as input as a str and then returns True or False,
respectively, if that input is a valid IPv4 address or not."""

import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matches = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    if matches:
        for group in matches.groups():
            if not (0 <= int(group) <=255):
                return False
        return True
    return False


if __name__ == "__main__":
    main()
