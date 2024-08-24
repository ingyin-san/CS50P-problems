"""prompts the user for a vanity plate and then output Valid if meets all of the requirements
or Invalid if it does not"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (2 <= len(s) <= 6 and
        s[0:2].isalpha() and
        valid_middle(s) and
        s.isalnum())

def valid_middle(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0' or not s[i:].isdigit():
                return False
            break
    return True

if __name__ == "__main__":
    main()
