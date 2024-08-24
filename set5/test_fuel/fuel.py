"""prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then
outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full."""


def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):

        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x > y and y != 0:
            raise ValueError

        return round(x/y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
