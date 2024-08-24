"""Expects zero or two command-line arguments,
prompts the user for a str of text, and
outputs that text in the desired font."""

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))
elif len(sys.argv) == 3:
    if (sys.argv[1] in ('-f', '--font')) and (sys.argv[2] in fonts):
        figlet.setFont(font = sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid Usage")

text = input("Input: ").strip()
print("Output: " + figlet.renderText(text))

