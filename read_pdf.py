# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('example.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# printing number of pages in pdf file
print(len(pdfReader.pages))

# creating a page object
for page in pdfReader.pages:
    # extracting text from page
    print(page.extract_text())

# closing the pdf file object
pdfFileObj.close()
