"""prompts the user for mass as an integer (in kilograms) and
outputs the equivalent number of Joules as an integer"""

m = int(input("m: "))
E = m * pow(300000000, 2)

print(E)
