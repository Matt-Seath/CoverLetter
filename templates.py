class GenericField():
    field = "technology"

    def __init__(self, data) -> None:
        self.company = data["company"]
        self.company_description = data["company_description"]
        self.company_mission = data["company_mission"]
        self.position = data["position"]
    

    def p1(self): 
        return f"""It is with enthusiasm I am writing to apply for the {self.position} position advertised by {self.company}. \
I'm passionate about {self.field} and I am delighted by the opportunity to apply my \
knowledge and further hone skills at {self.company}, {self.company_description}."""

    def p2(self):
        return """It is my hope to secure a position with a well-established corporation such as yours where I \
can build my career and become a valuable member of your team. I am currently studying a bachelor’s degree \
in data science at QUT and I have completed numerous online computer science courses that helped to prepare \
me for this position."""

    def p4(self):
        return """I am a detail-oriented leader with excellent communication skills that can function well in \
fast-paced environments. """

    def p5(self):
        return """I use my strong problem solving skills when issus arise and produce effective solutions. to communicate with non-technical \
clients in a way they can understand. I have excellent analytical skills and the ability to manage several \
projects at once while staying focused. I can follow orders and work well in a team but I also have the \
ability to work alone and still meet tight deadlines."""

    def p6(self):
        return f"""Thank you for your time and consideration. It would be an honor to join your team at {self.company} \
and use my skills to advance {self.company}'s mission to {self.company_mission}. I look forward to hearing from you in \
regards to my application."""


class SoftwareDev(GenericField):
    field = "software development"
    
    def p3(self):
        return f"""In addition to my studies, I have been engaged in web development for a long time, first as an amateur and now as a freelancer. \
As a result, I have the knowledge to help support software program development and assist in the design of \
software applications and the development of prototypes. I also have the ability to create user manuals \
containing the documentation of all codes. I have the training needed to perform system tests to look for \
areas that need improving. My experience also includes troubleshooting and correcting software problems in \
a fast and efficient manner."""


class Data(GenericField):
    field = "data"

     
    p1 = f"""It is with enthusiasm I am writing to apply for the {position} position. \
I'm passionate about {field} and I am delighted by the opportunity to apply my \
knowledge and further hone skills at {self.company}, {self.company_description}."""

    def p2(self):
        return """It is my hope to secure a position with a well-established corporation such as yours where I \
can build my career and become a valuable member of your team. I am currently studying a bachelor’s degree \
in data science at QUT and I have completed numerous online computer science courses that helped to prepare \
me for this position."""

    def p3(self):
        return """I strongly believe I am suited for this position as I am a detail-oriented team player with excellent written, communication and \
impersonal skills. My experience in retail also enabled me to excel in fast-paced environments \
with minimal supervision. In addition to my studies, I have several years of experience in entering data \
from multiple sources, and I take pride in my accuracy and speed in transcribing and transferring \
data into relevant data repositories. I am used to working with various types of source data for \
data entry purposes, and I also am very experienced with multitasking for other office duties as \
needed."""

    def p4(self):
        return None

    def p5(self):
        return None

    def p6(self):
        return f"""Thank you for your time and consideration. It would be an honor to join your team \
and use my skills to further {self.company}'s mission to put people first. I look forward to hearing from you in \
regards to my application."""


class DataScientist(GenericField):
    field = "data science"
