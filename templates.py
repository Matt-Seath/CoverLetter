class DefaultFields():
    field = "technology"

    def __init__(self, data) -> None:
        self.company = data["company"]
        self.desc = data["company_description"]
        self.mission = data["company_mission"]
        self.job = data["position"]
        self.genre = data["company_genre"] if data["company_genre"] else "corporation"
    

    def p1(self): 
        return f"""It is with enthusiasm that I am writing to apply for the {self.job} position. \
I'm passionate about {self.field} and I am delighted by the opportunity to apply my \
knowledge and further hone skills at {self.company}, {self.desc}."""

    def p2(self):
        return f"""It is my hope to secure a position with a well-established {self.genre} such as yours where I \
can build my career and become a valuable member of your team. I am currently studying a bachelor’s degree \
in data science at QUT and I have completed numerous online computer science courses that helped to prepare \
me for this position."""

    def p4(self):
        return f"""I am a detail-oriented leader with excellent communication skills that can function well in \
fast-paced environments. """

    def p5(self):
        return f"""I use my strong problem solving skills when issus arise and produce effective solutions. to communicate with non-technical \
clients in a way they can understand. I have excellent analytical skills and the ability to manage several \
projects at once while staying focused. I can follow orders and work well in a team but I also have the \
ability to work alone and still meet tight deadlines."""

    def p6(self):
        return f"""Thank you for your time and consideration. I'd love to join your team at {self.company} \
and use my skills to advance the company's mission to {self.mission}. I look forward to hearing from you in \
regards to my application."""


#----------------------------------------------------------------------------------------------------------------------------------


class SoftwareDev(DefaultFields):
    field = "software development"
    
    def p3(self):
        return f"""In addition to my studies, I have been engaged in web development for a l \
As a result, I have the knowledge to help support software program development and assist in the design of \
software applications and the development of prototypes. I also have the ability to create user manuals \
containing the documentation of all codes. I have the training needed to perform system tests to look for \
areas that need improving. My experience also includes troubleshooting and correcting software problems in \
a fast and efficient manner."""


#----------------------------------------------------------------------------------------------------------------------------------


class DataEntry(DefaultFields):
    field = "data"

    def p1(self): 
        return f"""It is with enthusiasm I am writing to apply for the {self.job} position. \
I believe my administrative experience and skillset makes me a great fit for this role and I am delighted by the opportunity to apply my \
knowledge and further hone skills at {self.company}, {self.desc}."""

    def p2(self):
        return f"""It is my goal to secure a position within a well-established {self.genre} such as yours where I \
can build my career and become a valuable member of your team. I am currently studying a bachelor’s degree \
in data science part-time at QUT while assisting management with administrative tasks at Ampol, where my fast \
typing speed and technical skills surrounding information systems has increased workflow productivity by over 30%."""

    def p3(self):
        return f"""I am a detail-oriented team player with excellent written, communication and \
interpersonal skills. My experience in retail and warehousing enabled me to excel working with deadlines \
in fast-paced environments with minimal supervision. In addition to my studies, I have several years of experience in entering data \
from multiple sources, and I take pride in my accuracy and speed in transcribing and transferring \
data into relevant data repositories."""

    def p4(self):
        return f"""I am proficient working with Microsoft Excel, SQL databases \
and other information systems. I am also capable of multitasking for other office duties as \
needed, all while upholding a high standard of professionalism and discretion that is necessary when working with company data."""

    def p5(self):
        return None

    def p6(self):
        return f"""Thank you for your time and consideration. I believe this opening is a great opportunity for me to excel and \
utilize my skills that advance {self.company}'s mission to {self.mission}. I look forward to hearing from you."""

#-----------------------------------------------------------------------------------------------------------------------------------

class DataScientist(DefaultFields):
    field = "data science"
