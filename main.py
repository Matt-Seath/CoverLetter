from distutils.log import error
from msilib.schema import Error
import os
import shutil
from datetime import datetime
from fpdf import FPDF
from dotenv import dotenv_values

# Get Personal Data from .env file in root directory
USER_DATA = dotenv_values(".env")

TODAY = datetime.now().strftime("%d %B, %Y")

# Pdf Formatting variables (mm)
FONT = "times"
FONT_SIZE = 10
MARGIN = 10
SPACING = 5
PAGE_WIDTH = 210
PAGE_HEIGHT = 297
TEXT_LENGTH = PAGE_WIDTH - ( MARGIN * 4 )

# Users Personal Information
FIRST_NAME = USER_DATA["FIRST_NAME"]
LAST_NAME = USER_DATA["LAST_NAME"]
MOBILE = USER_DATA["MOBILE"]
EMAIL = USER_DATA["EMAIL"]
ADDRESS_LINE_1 = USER_DATA["ADDRESS_L1"]
ADDRESS_LINE_2 = USER_DATA["ADDRESS_L2"]
POSTCODE = USER_DATA["POSTCODE"]
DOB = USER_DATA["DOB"]

PATH_TO_PROJECT = USER_DATA["PATH_TO_PROJECT"]
FILE_DESTINATION = USER_DATA["FILE_DESTINATION"]


def build_pdf(position, company, company_description, company_mission, bus_addr_l1, bus_addr_l2, recipient_title, recipient_first_name, recipient_last_name, recipient_position):
   
    # Intitial Page Configuration

    pdf = FPDF('P', 'mm', 'A4')          
    pdf.set_font(FONT, "", FONT_SIZE)
    pdf.add_page()                                  
    pdf.cell(0, 8, "", ln=True)

    #----------------------------------------------------------------------------------------
    # Header

    pdf.cell(180, SPACING, MOBILE, align="R", ln=True)

    pdf.cell(MARGIN)
    pdf.set_text_color(12, 140, 204)                      
    pdf.set_font(FONT, "B", FONT_SIZE + 10)
    pdf.cell(h=0,txt=FIRST_NAME)
    pdf.set_text_color(0, 0, 0)                                
    pdf.cell(h=0, txt=LAST_NAME, ln=True)                            
    pdf.set_text_color(0,0,0)

    pdf.set_font(FONT, "", FONT_SIZE)
    pdf.cell(180, SPACING, ADDRESS_LINE_1, align="R", ln=True)
    pdf.cell(180, SPACING, f"{ADDRESS_LINE_2} {POSTCODE}", align="R", ln=True)
    pdf.set_text_color(12, 140, 204)
    pdf.cell(180, SPACING, EMAIL, align="R", ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.line(21, 46, PAGE_WIDTH - 21, 46)

    #------------------------------------------------------------------------------------------
    # Date

    pdf.cell(0, 15, "", ln=True)
    pdf.cell(MARGIN)                                                                          
    pdf.cell(TEXT_LENGTH, 20, TODAY, ln=True)
    
    #------------------------------------------------------------------------------------------
    # Recipient/Company Name, address

    pdf.cell(MARGIN)
    if recipient_last_name and recipient_title:
        pdf.set_font(FONT, "B", FONT_SIZE)
        pdf.cell(TEXT_LENGTH, SPACING, f"{recipient_title} {recipient_first_name} {recipient_last_name}, {recipient_position}", ln=True)
        pdf.set_font(FONT, "", FONT_SIZE)     
        pdf.cell(MARGIN)

    pdf.cell(TEXT_LENGTH, SPACING, company, ln=True)

    pdf.cell(MARGIN)
    pdf.cell(TEXT_LENGTH, SPACING, bus_addr_l1, ln=True)              

    pdf.cell(MARGIN)
    pdf.cell(TEXT_LENGTH, SPACING, bus_addr_l2, ln=True)

    #------------------------------------------------------------------------------------------
    # Title / Subject

    pdf.cell(MARGIN)
    pdf.cell(TEXT_LENGTH, 25, f"RE: Expression of interest for { position } position", ln=True)

    pdf.cell(MARGIN)                                                               
    if recipient_title and recipient_last_name:
        pdf.cell(TEXT_LENGTH, SPACING, f"Dear {recipient_title} {recipient_last_name},", ln=True)
    else:
        pdf.cell(TEXT_LENGTH, SPACING, "Dear Hiring Manager,", ln=True)
    pdf.cell(0, SPACING, "", ln=True)

    #------------------------------------------------------------------------------------------
    # Body

    pdf.cell(MARGIN)                                                                         
    pdf.multi_cell(TEXT_LENGTH, SPACING, f"""I'm excited to be applying for the {position} position at {company}. When it comes to software development, there is always room to grow and discover new things. Designing programs that helps make tasks and goals easier to achieve is something I'm passionate about, and I am delighted by the opportunity to apply my knowledge at {company}, {company_description}.""")

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, f"""I had taken an interest in Programming from a young age, where I would frequenty write scripts to automate the boring and repetitive tasks from my computer. I enjoy using my strong problem-solving skills to overcome challenges, and programming gives me the opportunity to constantly challenge myself and improve my skills as a developer.""")

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, f"""Today, I'm a self-motivated and energetic back-end developer with a focus on automating tasks and maintaining servers for web applications. I specialise in Python and have experience working with both Django and Flask frameworks. I'm a fast-learner and a lover of data, knowledgeable in a wide-array of other software and technologies including C, Kotlin, Android SDK and JavaScript.""")
    
    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, f"""Thank you for your time and consideration. I'm looking forward to learning more about the {position} position and about {company}. As a software Developer, my goal is to continually increase my programming skills in order to present better solutions to my employers and their clients. I enjoy uncovering new ideas and would use them to advance {company}'s mission to {company_mission}.""")

    #------------------------------------------------------------------------------------------
    #Sign

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, f"""Sincerely,""")                            

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, f"""{FIRST_NAME} {LAST_NAME}""")

    #------------------------------------------------------------------------------------------
    # Return pdf object

    return pdf


def save_pdf(pdf, company):
    
    pdf.output(f"CoverLetter ({company}).pdf")
    try:
        file_path = os.path.join(PATH_TO_PROJECT, f"CoverLetter ({company}).pdf")
        destination_path = os.path.join(FILE_DESTINATION, f"CoverLetter ({company}).pdf")
        shutil.move(file_path, destination_path)
    except Error:
        print(error)
        return 1
    return 0


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    company = input("Company Name:  ").strip().title()
    company_description = input("Company Description: e.g. (A leader of cloud storage in Australia):  ").strip()
    company_mission = input("Companys Mission e.g. (deliver viable solutions for digital storage):  ").strip()
    business_address_l1 = input("Business Address, Line 1:  ").strip().title()
    business_address_l2 = input("Business Address, Line 2:  ").strip().title()
    position = input("Job Position:  ").strip().title()
    while True:
        recipient_exists = input("Add Recipient? (y)=YES, (n)=NO:  ").strip().lower()
        if recipient_exists == "y":
            while True:
                ans = input("Recipients Title (mr, mrs, ms, dr):  ").strip().lower()
                if ans == "mr" or ans == "mrs" or ans == "ms" or ans == "dr":
                    recipient_title = ans.title() + "."
                    break
            recipient_first_name = input("First name of Recipient:  ").strip().title()
            recipient_last_name = input("Last name of Recipient:  ").strip().title()
            recipient_position = input("Position of Recipient:  ").strip().title()
            break
        if recipient_exists == "n":
            recipient_title = recipient_first_name = recipient_last_name = recipient_position = None
            break

    pdf = build_pdf(position, company, company_description, company_mission, business_address_l1, business_address_l2, recipient_title, recipient_first_name, recipient_last_name, recipient_position)
    save_pdf(pdf, company)
    return 0

if __name__ == "__main__":
    main()