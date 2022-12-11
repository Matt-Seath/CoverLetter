import os
import shutil
from datetime import datetime
from fpdf import FPDF
from dotenv import dotenv_values

from templates import *


# Get Personal Data from .env file in root directory
USER_DATA = dotenv_values(".env")

TODAY = datetime.now().strftime("%d %B, %Y")

# Pdf Formatting variables (mm)
FONT = "EBGaramond"
FONT_2 = "EBGaramond bold"
FONT_SIZE = 12
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


def build_pdf(template, data):
   
    # Intitial Page Configuration 
    pdf = FPDF('P', 'mm', 'A4')      
    pdf.add_font(FONT, "", PATH_TO_PROJECT + "EBGaramond.ttf")
    pdf.add_font(FONT_2, "", PATH_TO_PROJECT + "EBGaramond_bold.ttf")
    pdf.set_font(FONT_2, "", FONT_SIZE + 10)
    pdf.add_page()                                  
    pdf.cell(0, MARGIN * 2, "", ln=True)

    #----------------------------------------------------------------------------------------
    # Header

    pdf.cell(MARGIN)
    pdf.cell(h=0,txt=FIRST_NAME.upper())
    pdf.cell(h=0, txt=LAST_NAME.upper(), ln=True)                            
    
    pdf.set_font(FONT, "", FONT_SIZE)
    pdf.cell(180, SPACING, 
        f"{ADDRESS_LINE_1.title()}, {ADDRESS_LINE_2} {POSTCODE}  |", align="R", ln=True)
    pdf.cell(180, SPACING, MOBILE + "  |", align="R", ln=True)
    pdf.cell(180, SPACING, EMAIL + "  |", align="R", ln=True)

    #------------------------------------------------------------------------------------------
    # Date

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)                                                                          
    pdf.cell(TEXT_LENGTH, 20, "    " + TODAY, ln=True)
    
    #------------------------------------------------------------------------------------------
    # Recipient/Company Name, address

    pdf.cell(MARGIN)
    if data["recipient_last_name"] and data["recipient_title"]:
        pdf.cell(TEXT_LENGTH, SPACING, f"""    \
{data["recipient_title"]} {data["recipient_first_name"]} \
{data["recipient_last_name"]}, {data["recipient_position"]}""", ln=True)

        pdf.cell(MARGIN)

    pdf.cell(TEXT_LENGTH, SPACING, "    " + data["company"], ln=True)

    pdf.cell(MARGIN)
    pdf.cell(TEXT_LENGTH, SPACING, "    " + data["business_address_l1"], ln=True)              

    pdf.cell(MARGIN)
    pdf.cell(TEXT_LENGTH, SPACING, "    " + data["business_address_l2"], ln=True)

    #------------------------------------------------------------------------------------------
    # Title / Subject

    pdf.cell(MARGIN)
    pdf.cell(TEXT_LENGTH, 25, 
        f"""RE: Expression of interest for { data["position"] } position""", ln=True)

    pdf.cell(MARGIN)                                                               
    if data["recipient_title"] and data["recipient_last_name"]:
        pdf.cell(TEXT_LENGTH, SPACING, 
            f"""Dear {data["recipient_title"]} {data["recipient_last_name"]},""", ln=True)
    else:
        pdf.cell(TEXT_LENGTH, SPACING, "Dear Hiring Manager,", ln=True)
    pdf.cell(0, SPACING, "", ln=True)

    #------------------------------------------------------------------------------------------
    # Body

    pdf.cell(MARGIN)                                                                         
    pdf.multi_cell(TEXT_LENGTH, SPACING, template.p1(data))

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, template.p2(data))

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, template.p3(data))

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, template.p4(data))
    
    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, template.p5(data))

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, template.p6(data))

    #------------------------------------------------------------------------------------------
    #Sign

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, f"""Sincerely,""")                            

    pdf.cell(0, SPACING, "", ln=True)
    pdf.cell(MARGIN)
    pdf.multi_cell(TEXT_LENGTH, SPACING, f"""{FIRST_NAME.title()} {LAST_NAME.title()}""")

    #------------------------------------------------------------------------------------------
    # Return pdf object

    return pdf


def save_pdf(pdf, company):
    
    pdf.output(f"CoverLetter ({company}).pdf")
    try:
        file_path = os.path.join(PATH_TO_PROJECT, f"CoverLetter ({company}).pdf")
        destination_path = os.path.join(FILE_DESTINATION, f"CoverLetter ({company}).pdf")
        shutil.move(file_path, destination_path)
    except:
        print("Error")
        return 1
    return 0


def main():
    data = {}
    os.system('cls' if os.name == 'nt' else 'clear')
    data["company"] = input("Company Name:  ").strip().title()
    data["company_description"] = \
        input("Company Description: e.g. (A leader of cloud storage in Australia):  ").strip()
    data["company_mission"] = \
        input("Companys Mission e.g. (deliver viable solutions for digital storage):  ").strip()
    data["business_address_l1"] = input("Business Address, Line 1:  ").strip().title()
    data["business_address_l2"] = input("Business Address, Line 2:  ").strip().title()
    data["position"] = input("Job Position:  ").strip().title()
    while True:
        data["field"] = input("Industry Field (data, dev):  ").strip().lower()
        if data["field"] == "data":
            template = DataScience()
            break
        if data["field"] == "dev":
            template = SoftwareDev()
            break
    while True:
        recipient_exists = input("Add Recipient? (y)=YES, (n)=NO:  ").strip().lower()
        if recipient_exists == "y":
            while True:
                ans = input("Recipients Title (mr, mrs, ms, dr):  ").strip().lower()
                if ans == "mr" or ans == "mrs" or ans == "ms" or ans == "dr":
                    data["recipient_title"] = ans.title() + "."
                    break
            data["recipient_first_name"] = input("First name of Recipient:  ").strip().title()
            data["recipient_last_name"] = input("Last name of Recipient:  ").strip().title()
            data["recipient_position"] = input("Position of Recipient:  ").strip().title()
            break
        if recipient_exists == "n":
            data["recipient_title"] = data["recipient_first_name"] \
                = data["recipient_last_name"] = data["recipient_position"] = None
            break
    
    print(data)
    pdf = build_pdf(template, data)
    save_pdf(pdf, data["company"])
    return 0

if __name__ == "__main__":
    main()