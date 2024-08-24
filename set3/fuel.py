"""prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then
outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full."""

while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if x > y:
            continue

        percent = round(x/y * 100)
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
        break
    except (ValueError, ZeroDivisionError):
        pass
