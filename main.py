import string
from datetime import datetime
from fpdf import FPDF
from dotenv import dotenv_values

# Get Personal Data from .env file in root directory
USER_DATA = dotenv_values(".env")

TODAY = datetime.now().strftime("%d %B, %Y")


# Pdf Formatting variables (mm)
FONT_SIZE = 10
MARGIN = 10
SPACING = 6
FONT = "times"
PAGE_WIDTH = 210
PAGE_HEIGHT = 297
TEXT_LENGTH = 170

# Users Personal Information
FIRST_NAME = USER_DATA["FIRST_NAME"]
LAST_NAME = USER_DATA["LAST_NAME"]
MOBILE = USER_DATA["MOBILE"]
EMAIL = USER_DATA["EMAIL"]
ADDRESS_LINE_1 = USER_DATA["ADDRESS_L1"]
ADDRESS_LINE_2 = USER_DATA["ADDRESS_L2"]
POSTCODE = USER_DATA["POSTCODE"]
DOB = USER_DATA["DOB"]



def build_pdf(position, company, bus_addr_l1, bus_addr_l2, recipient_title, recipient_first_name, recipient_last_name, recipient_position):

    #----------------------------------------------------------------------------------------

    pdf = FPDF('P', 'mm', 'A4')          
    pdf.set_font(FONT, "", FONT_SIZE)
    pdf.add_page()                                  # Initial Page Settings
    pdf.cell(0, 8, "", ln=True)

    #----------------------------------------------------------------------------------------

    pdf.cell(180, SPACING, MOBILE, align="R", ln=True)

    pdf.cell(MARGIN)
    pdf.set_text_color(12, 140, 204)                      
    pdf.set_font(FONT, "B", FONT_SIZE + 20)
    pdf.cell(h=0,txt=FIRST_NAME)
    pdf.set_text_color(0, 0, 0)                                
    pdf.cell(h=0, txt=LAST_NAME, ln=True)                            # Header
    pdf.set_text_color(0,0,0)

    pdf.set_font(FONT, "", FONT_SIZE)
    pdf.cell(180, SPACING, ADDRESS_LINE_1, align="R", ln=True)
    pdf.cell(180, SPACING, f"{ADDRESS_LINE_2} {POSTCODE}", align="R", ln=True)
    pdf.set_text_color(12, 140, 204)
    pdf.cell(180, SPACING, EMAIL, align="R", ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.line(21, 46, PAGE_WIDTH - 21, 48)

    #------------------------------------------------------------------------------------------

    pdf.cell(0, 15, "", ln=True)
    pdf.cell(MARGIN)                                                                          # Date
    pdf.cell(TEXT_LENGTH, 20, TODAY, ln=True)
    
    #------------------------------------------------------------------------------------------

    pdf.cell(MARGIN)
    if recipient_last_name and recipient_title:
        pdf.set_font(FONT, "B", FONT_SIZE)
        pdf.cell(TEXT_LENGTH, SPACING, f"{recipient_title} {recipient_first_name} {recipient_last_name}, {recipient_position}", ln=True)
        pdf.set_font(FONT, "", FONT_SIZE)     
        pdf.cell(MARGIN)

    pdf.cell(TEXT_LENGTH, SPACING, company, ln=True)

    pdf.cell(MARGIN)
    pdf.cell(TEXT_LENGTH, SPACING, bus_addr_l1, ln=True)               # Recipient/Company Name, address

    pdf.cell(MARGIN)
    pdf.cell(TEXT_LENGTH, SPACING, bus_addr_l2, ln=True)

    #------------------------------------------------------------------------------------------

    pdf.cell(MARGIN)
    pdf.cell(TEXT_LENGTH, 25, f"RE: Expression of interest for { position } position", ln=True)

    pdf.cell(MARGIN)                                                                # Title / Subject
    if recipient_title and recipient_last_name:
        pdf.cell(TEXT_LENGTH, SPACING, f"Dear {recipient_title} {recipient_last_name},", ln=True)
    else:
        pdf.cell(TEXT_LENGTH, SPACING, "Dear Hiring Manager,", ln=True)

    #------------------------------------------------------------------------------------------

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)                                                                            # Body
    pdf.multi_cell(TEXT_LENGTH, SPACING, f"""I'm excited to be applying for the {position} position at {company}. When it comes to software development, there is always room to grow and discover new things. Designing programs that help make tasks and goals easier to achieve is something I'm passionate about.""")

    #------------------------------------------------------------------------------------------

    pdf.output("CoverLetter.pdf")
    return 0

def main():
    company = input("Company Name:  ").strip().title()
    business_address_l1 = input("Business Address, Line 1:  ").strip().title()
    business_address_l2 = input("Business Address, Line 2:  ").strip().title()
    position = input("Job Position:  ").strip().title()
    while True:
        recipient_exists = input("Add Recipient? (y)=YES, (n)=NO:  ").strip()
        if recipient_exists.lower() == "y":
            while True:
                ans = input("Recipients Title (mr, mrs, ms, dr):  ").strip()
                if ans == "mr" or ans == "mrs" or ans == "ms" or ans == "dr":
                    recipient_title = ans.title() + "."
                    break
            recipient_first_name = input("First name of Recipient:  ").strip().title()
            recipient_last_name = input("Last name of Recipient:  ").strip().title()
            recipient_position = input("Position of Recipient:  ").strip().title()
            break
        if recipient_exists.lower() == "n":
            recipient_title = recipient_first_name = recipient_last_name = recipient_position = None
            break

    build_pdf(position, company, business_address_l1, business_address_l2, recipient_title, recipient_first_name, recipient_last_name, recipient_position)

if __name__ == "__main__":
    main()