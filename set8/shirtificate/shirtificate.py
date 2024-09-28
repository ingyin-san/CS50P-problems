#prompts the user for their name and outputs a CS50 shirtificate in a file called shirtificate.pdf

from fpdf import FPDF


pdf = FPDF(orientation = "portrait", format = "A4")
pdf.add_page()

pdf.set_font("helvetica", size = 40)
pdf.cell(0, 20, "CS50 Shirtificate", align = "C")
pdf.ln(20)

pdf.image("shirtificate.png", x = 1, y = 40)

pdf.set_text_color(255, 255, 255)
pdf.cell(0, 150, input("Name: ") + " took CS50", align = "C")

pdf.output("shirtificate.pdf")

