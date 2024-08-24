"""expects exactly two command-line arguments:
in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program then overlay shirt.png (which has a transparent background) on the input
 after resizing and cropping the input to be the same size, saving the result as its output."""

import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    format = [".jpg", ".jpeg", ".png"]
    if "." in sys.argv[1] and "." in sys.argv[2]:
        input_extension = os.path.splitext(sys.argv[1])[1].lower()
        output_extension = os.path.splitext(sys.argv[2])[1].lower()
        if (not (input_extension in format or output_extension in format)):
            sys.exit("Invalid input")

        if input_extension != output_extension:
            sys.exit("Input and output have different extensions")

        try:
            shirt = Image.open("shirt.png")
            size = shirt.size
            photo = Image.open(sys.argv[1])

            pic = ImageOps.fit(photo, size)
            pic.paste(shirt, shirt)
            pic.save(sys.argv[2])
        except (FileNotFoundError):
            sys.exit("File does not exist")
    else:
        sys.exit("Invalid input")


