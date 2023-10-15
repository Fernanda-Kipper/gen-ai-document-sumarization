# from PyPDF2 import PdfReader
from pypdf import PdfReader

import docx
from simplify_docx import simplify

from models.bart import create_bart_summarizer

def break_text_in_sequences(extracted_text,max_length_sequence):
    segments = []
    for text in extracted_text:
        for i in range(0, len(text), max_length_sequence):
            segment = text[i:i + max_length_sequence]
            segments.append(segment)

    return segments

def extract_text_recursive(docx_json):
    text_list = []

    if isinstance(docx_json, dict):
        if docx_json.get('TYPE') == 'text':
            text_list.append(docx_json.get('VALUE', ''))
        else:
            for key, value in docx_json.items():
                text_list.extend(extract_text_recursive(value))
    elif isinstance(docx_json, list):
        for item in docx_json:
            text_list.extend(extract_text_recursive(item))

    return text_list

def extract_text_from_pdf(filename):
    reader = PdfReader('./inputs/' + filename)
    extracted_text = []

    for page in reader.pages:
        text = page.extract_text()
        extracted_text.append(text)

    return extracted_text

def extract_text_from_docx(filename):
    document = docx.Document('./inputs/' + filename)
    my_doc_as_json = simplify(document)

    extracted_text = extract_text_recursive(my_doc_as_json)
    print(extracted_text)

    return extracted_text

# raw_text = extract_text_from_pdf('once-upon-a-time-test.pdf')
raw_text = extract_text_from_docx('once-upon-a-time-test.docx')
processed_text = break_text_in_sequences(raw_text, 1024)
bart_summarizer = create_bart_summarizer()

print(bart_summarizer(processed_text, max_length=130, min_length=30, do_sample=False))
