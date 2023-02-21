from PyPDF2 import PdfReader

from constants import ROLE_TYPE__FE, ROLE_TYPE__PYTHON_BE
from util import get_scoring_data, score_text, refined_text, sort_scores

# creating a pdf file object
pdfFileObj = open('example.pdf', 'rb')

# creating a pdf reader object
pdfReader: PdfReader = PdfReader(pdfFileObj)

# get scoring metadata
score_map_fe = get_scoring_data(ROLE_TYPE__FE)
score_map_be = get_scoring_data(ROLE_TYPE__PYTHON_BE)
page_scores_fe = dict()
page_scores_be = dict()

# read CVs page by pages (skip first 2 pages)
start = 2
end = len(pdfReader.pages)

# score each page by given score map
while start < end:
    text = refined_text(pdfReader.pages[start].extract_text())
    page_scores_fe["Page {}".format(start)] = score_text(text, score_map_fe)
    page_scores_be["Page {}".format(start)] = score_text(text, score_map_be)
    start += 1

# candidates = get_candidates_from_text(pdfReader, 2)
# cv_page_map = dict()
# for page in pdfReader.pages:
#     page_txt = page.extract_text().strip().lower()
#     for candidate in candidates:
#         if candidate in page_txt:
#             if candidate in cv_page_map:
#                 cv_page_map[candidate] += page_txt
#             else:
#                 cv_page_map[candidate] = page_txt

# Results
print('Top 5 scoring resumes (FE): ')
print(sort_scores(page_scores_fe, 5))
print('Top 5 scoring resumes (BE): ')
print(sort_scores(page_scores_be, 5))

# closing the pdf file object
pdfFileObj.close()
