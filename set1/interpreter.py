"""prompts the user for an arithmetic expression and then
calculates and outputs the result as a floating-point value formatted to one decimal place."""

x, y, z = input("Expression: ").strip().split(" ")

x = float(x)
z = float(z)

match y:
    case "+":
        print(f"{x + z:.1f}")
    case "-":
        print(f"{x - z:.1f}")
    case "*":
        print(f"{x * z:.1f}")
    case "/":
        print(f"{x / z:.1f}")

