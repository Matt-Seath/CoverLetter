from fpdf import FPDF
from dotenv import dotenv_values


NAME = dotenv_values("NAME")
MOBILE = dotenv_values("MOBILE")
EMAIL = dotenv_values("EMAIL")
DOB = dotenv_values("DOB")
SKILLS = dotenv_values("SKILLS")



pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font("times", "B", 20)


pdf.cell(0, 20, "", ln=True)
pdf.cell(100, 10, "")
pdf.cell(50, 11, NAME, ln=True)

pdf.set_font("times", "", 14)
pdf.cell(100, 0, "")
pdf.cell(18, 6, "Email:")
pdf.cell(50, 6, EMAIL, ln=True)

pdf.cell(100, 0, "")
pdf.cell(18, 6, "Mobile:")
pdf.cell(50, 6, MOBILE, ln=True)

pdf.output("CoverLetter.pdf")
