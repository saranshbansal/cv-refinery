# importing required modules
import PyPDF2
from scoring import get_scoring_data
from constants import ROLE_TYPES


# creating a pdf file object
pdfFileObj = open('example.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# printing number of pages in pdf file
page_count = len(pdfReader.pages)

# Get scoring data
score_one = get_scoring_data(ROLE_TYPES[0])
score_two = get_scoring_data(ROLE_TYPES[0])
page_score = {}

# extracting text from page
index = 0
while index < 10:
    page_data = pdfReader.pages[index]
    print(page_data.extract_text().strip().lower())
    index += 1

# closing the pdf file object
pdfFileObj.close()
