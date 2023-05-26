from linkedin_pdf_extractor.pdfstructure.hierarchy.parser import HierarchyParser
from linkedin_pdf_extractor.pdfstructure.source import FileSource
# from linkedin_pdf_extractor.pdfstructure.printer import JsonFilePrinter
import json
from linkedin_pdf_extractor.pdfstructure.model.document import Section
from typing import List
import pandas as pd
import re



class Summary:
    def __init__(self):
        self.description = []
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)

class Contact:
    def __init__(self):
        self.mobile = ""
        self.email = ""
        self.link = ""
        self.description = ""
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)


class Experience:
    def __init__(self):
        self.id = 0
        self.companyName = ""
        self.position = ""
        self.date = ""
        self.description = ""
        self.location = ""
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)

class Education:
    def __init__(self):
        self.course = ""
        self.university = ""
        self.date = ""
        self.description = []
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)


class User:
    def __init__(self):
        self.name = ""
        self.contact = Contact()
        self.title = ""
        self.location = ""
        self.summary = ""
        self.skills = []
        self.experience = []
        self.education = [] 
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)

# Dict = {}
Data = []


def pdf_to_json(pdfpath:str):
    parser = HierarchyParser()
    source = FileSource(pdfpath)
    document = parser.parse_pdf(source)

    traverse(document.elements, document.elements[0].level)
    for d in Data:
        print(d)
    df = pd.DataFrame(Data)
    # print(df)
    dtoData = createData(df)
    # print("The variable, name : ", dtoData.name)
    # print("The variable, mobile : ", dtoData.contact.mobile)
    # print("The variable, email : ", dtoData.contact.email)
    # print("The variable, title : ", dtoData.title)
    # print("The variable, summary : ", dtoData.summary)
    jsonStr = dtoData.toJSON()
    print(jsonStr)
    return jsonStr


def traverse(elements: List[Section], level, parent=None):
    # print(len(elements))
    i=0
    for e in elements:
        if (e.heading.text == "Summary" or e.heading.text == "Contact" or
           e.heading.text == "Top Skills" or e.heading.text == "Experience" or e.heading.text == "Education"):
            parent = e.heading.text
        # print(e.heading)
        
        Data.append({"level": level+1, "text": e.heading.text, "type": parent,
                    "mean_size": e.heading.style.mean_size, "max_size": e.heading.style.max_size, "index": i})
        i=i+1
        # print("Level: ", level, element)
        traverse(e.children, e.level, parent)


def createData(data):
    user = User()
    summary = Summary()
    contact = Contact()
    i = 0
    for index, row in data.iterrows():
        if (row['level'] == 1 and row["mean_size"] == 26.0 and row["max_size"] == 26.0):
            user.name = row["text"]
        elif (row['level'] == 1 and row["mean_size"] == 12.0 and row["max_size"] == 12.0):
            user.title = ' '.join(map(str, row["text"].split('\n')[0:-1]))
        elif ((row['level'] == 2 or row['level'] == 3) and 11.8 < row["max_size"] < 12.5 and row["type"] == "Summary"):
            summary.description.append(row["text"])
        elif (row['level'] == 3 and 10.4 < row["max_size"] < 10.6 and row["type"] == "Contact"):
            contact.description = row["text"]
        elif ((row['level'] == 2 or row['level'] == 1) and 10.4 < row["max_size"] < 10.6 and row["type"] == "Top Skills"):
            user.skills.append(row["text"])
        elif(row["type"] == "Experience"):
            # if()
            parseExperience(row, user)
        elif (row["type"] == "Education"):
            parseEducation(row, user)
    
    user.summary = ' '.join(map(str, summary.description))
    
    return user

def parseExperience(row, user):
    expLength = len(user.experience)
    exp = Experience() if expLength == 0 else user.experience[expLength-1]
    if (row["max_size"] <= 12.9 and row["max_size"] >= 11.9):
        exp = Experience()
        expElements = row['text'].split('\n')
        if(len(expElements) == 1):
            exp.companyName = expElements[0]
        elif(len(expElements) == 2):
            exp.companyName = expElements[0]
            exp.date = expElements[1].replace('\xa0','')
        elif(len(expElements) == 3):
            exp.companyName = expElements[0]
            exp.position = expElements[1]
            exp.date = expElements[2].replace('\xa0','')
        elif(len(expElements) == 4 ):
            exp.companyName = expElements[0]
            exp.position = expElements[1]
            exp.date = expElements[2].replace('\xa0','')
            exp.location = expElements[3]
        user.experience.append(exp)
    elif(row["max_size"] > 9.0 and row["max_size"] < 11.5):
        user.experience[expLength-1].description += row["text"]

def parseEducation(row, user):
    eduLength = len(user.education)
    edu = Education() if eduLength == 0 else user.education[eduLength-1]
    
    if (row["max_size"] <= 12.9 and row["max_size"] >= 11.9):
        edu = Education()
        edu.university = row['text']
        user.education.append(edu)
    elif(row["max_size"] < 10.6 and row["max_size"] > 10.2 ):
        user.education[eduLength-1].course += row["text"]

pdf_to_json("/home/pk/Documents/gig-banking/test_linkdin_package/rashmi.pdf")
#pdf_to_json("/Users/rishav/Downloads/rashmi_linkedin.pdf")