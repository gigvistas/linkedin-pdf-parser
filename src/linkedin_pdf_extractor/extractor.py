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

    a = document.elements
    #print(a[0])
    #print(a[0].children[1])

    traverse(document.elements, document.elements[0].level)
    df = pd.DataFrame(Data)
    print(df)
    dtoData = createData(df)
    print("The variable, name : ", dtoData.name)
    print("The variable, mobile : ", dtoData.contact.mobile)
    print("The variable, email : ", dtoData.contact.email)
    print("The variable, title : ", dtoData.title)
    print("The variable, summary : ", dtoData.summary)
    jsonStr = dtoData.toJSON()
    print(jsonStr)
    return jsonStr


def traverse(elements: List[Section], level, parent=None):
    # print(len(elements))
    for e in elements:
        if (e.heading.text == "Summary" or e.heading.text == "Contact" or
           e.heading.text == "Top Skills" or e.heading.text == "Experience" or e.heading.text == "Education"):
            parent = e.heading.text
        # print(e).
        Data.append({"level": level+1, "text": e.heading.text, "type": parent,
                    "mean_size": e.heading.style.mean_size, "max_size": e.heading.style.max_size})
        # print("Level: ", level, element)
        traverse(e.children, e.level, parent)


def createData(data):
    user = User()
    summary = Summary()
    contact = Contact()
    experience = Experience()
    education = Education()
    i = 0
    for index, row in data.iterrows():
        if (row['level'] == 1 and row["mean_size"] == 26.0 and row["max_size"] == 26.0):
            user.name = row["text"]
        elif (row['level'] == 1 and row["mean_size"] == 12.0 and row["max_size"] == 12.0):
            user.title = row["text"].split('\n')[0]
        elif (row['level'] == 2 and row["mean_size"] == 12.0 and row["max_size"] == 12.0 and row["type"] == "Summary"):
            summary.description.append(row["text"])
        elif (row['level'] == 3 and row["mean_size"] == 10.5 and row["max_size"] == 10.5 and row["type"] == "Contact"):
            contact.description = row["text"]
        elif (row['level'] == 3 and row["mean_size"] == 10.5 and row["max_size"] == 10.5 and row["type"] == "Top Skills"):
            user.skills.append(row["text"])
        elif(row['level'] == 2 and row["type"] == "Experience"):
            parseExperience(row, user)
        # elif (row["type"] == "Education"):
        #     education.description.append(row["text"])

    user.summary = ' '.join(map(str, summary.description))

    # mobile_pattern = r'\+(\d{1,2})?\s*\d{9,10}\s*\((Mobile)\)'
    # email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # match = re.search(mobile_pattern, contact.description)
    # if match:
    #     contact.mobile = match.group(0)
    #     contact.email = re.search(
    #         email_pattern, contact.description[match.end():]).group(0)
    # else:
    #     contact.email = re.search(email_pattern, contact.description).group(0)
    # user.contact = contact

    return user

def parseExperience(row, user):
    expLength = len(user.experience)
    exp = Experience() if expLength == 0 else user.experience[expLength-1]
    
    if (row["max_size"] == 12.0):
        exp = Experience()
        expElements = row['text'].split('\n')
        if(len(expElements) == 2):
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
    elif(row["max_size"] > 9.0):
        user.experience[expLength-1].description += row["text"]

#pdf_to_json("/Users/rishav/code/github/gigvistas/linkedin-pdf-parser/tests/resources/profile.pdf")
#pdf_to_json("/Users/rishav/Downloads/rishav_linkedin.pdf")