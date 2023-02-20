from PyPDF2 import PdfReader

from constants import *


def get_scoring_data(role: str) -> dict:
    if role == ROLE_TYPE__FE:
        return PROFILE_FE_SCORE_MAP
    elif role == ROLE_TYPE__PYTHON_BE:
        return PROFILE_BE_SCORE_MAP
    else:
        print('Please choose a valid role!')


def refined_text(text: str) -> str:
    return text.strip().lower()


def score_text(text: str, score_map_fe: dict) -> int:
    agg_score = 0
    for key, value in score_map_fe.items():
        if key.lower() in text:
            agg_score += value

    return agg_score


def get_candidates_from_text(reader: PdfReader, end: int, raw_text='') -> list:
    start = 0
    while start < end:
        raw_text += reader.pages[start].extract_text()
        start += 1

    return raw_text.strip().lower().split('\n \n')


def get_attachments(reader: PdfReader) -> dict:
    """
    Retrieves the file attachments of the PDF as a dictionary of file names
    and the file data as a bytestring.
    :return: dictionary of filenames and bytestrings
    """
    catalog = reader.trailer["/Root"]
    print(catalog['/Names'])
    fileNames = catalog['/Names']['/EmbeddedFiles']['/Kids'][0].getObject()['/Names']
    attachments = {}
    for f in fileNames:
        if isinstance(f, str):
            name = f
            dataIndex = fileNames.index(f) + 1
            fDict = fileNames[dataIndex].getObject()
            fData = fDict['/EF']['/F'].getData()
            attachments[name] = fData

    return attachments
