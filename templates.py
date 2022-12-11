class GenericField():
    field = "technology"

    def p1(self, data): 
        return f"""I am writing to apply for the {data["position"]} job opening advertised by {data["company"]}. \
I'm passionate about {self.field}, and I am delighted by the opportunity to apply my \
knowledge at {data["company"]}, {data["company_description"]}."""

    def p2(self, data):
        return """It is my hope to secure a position with a well-established corporation such as yours where I \
can build my career and become a valuable member of your team. I am currently studying a bachelor’s degree \
in data science at QUT and I have completed numerous online computer science courses that helped to prepare \
me for this position."""

    def p4(self, data):
        return """I have great communication skills with the ability to provide friendly and professional \
customer service and to relay suggestions, requests and other information that can help to improve \
performance, speed and to make applications more user-friendly."""

    def p5(self, data):
        return """I have the ability to solve problems as they occur and to communicate with non-technical \
clients in a way they can understand. I have excellent analytical skills and the ability to manage several \
projects at once while staying focused. I can follow orders and work as a team without any problems but I \
also have the ability to work alone and still meet tight deadlines."""

    def p6(self, data):
        return """I hope to meet with you soon to talk about this position and further explore my experience and \
skills in more detail. Please don't hesitate to call my mobile 0407 200 890 to schedule an interview."""


class SoftwareDev(GenericField):
    field = "software development"
    
    def p3(self, data):
        return """I have the knowledge to help support software program development and assist in the design of \
software applications and the development of prototypes. I also have the ability to create user manuals \
containing the documentation of all codes. I have the training needed to perform system tests to look for \
areas that need improving. My experience also includes troubleshooting and correcting software problems in \
a fast and efficient manner."""


class DataScience(GenericField):
    field = "data science"

    def p3(self, data):
        return "hi there"