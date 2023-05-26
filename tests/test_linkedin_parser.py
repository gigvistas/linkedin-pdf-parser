from ..src.linkedin_pdf_extractor.extractor import pdf_to_json

def test_pdf_to_json():
    pdfpath = './resources/profile.pdf'
    user = pdf_to_json(pdfpath)
    print(user)
    
test_pdf_to_json()