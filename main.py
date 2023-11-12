# from PyPDF2 import PdfReader
from pypdf import PdfReader

import docx
from simplify_docx import simplify

from models.bart import create_bart_summarizer
from models.mt5 import create_mt5_summarizer
from models.t5 import create_t5_summarizer
from models.pegasus import create_pegasus_summarizer

def break_text_in_sequences(extracted_text,max_length_sequence):
    segments = []
    for text in extracted_text:
        text = text.replace("\n", " ")
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
    return extracted_text

def concat_summaries(summaries_list):
    final_summary = ""
    for summary in summaries_list:
        final_summary += summary['summary_text']
    return final_summary

def calculate_max_length_of_summary(text_list):
    min_text_length = 1024
    for text in text_list:
        if(len(text.strip()) < min_text_length):
            min_text_length = len(text.strip())
    return int(min_text_length/2)

raw_text = extract_text_from_pdf('transformers.pdf')
raw_text = extract_text_from_docx('once-upon-a-time-test.docx')
processed_text = break_text_in_sequences(raw_text, 1024)
max_length =  calculate_max_length_of_summary(processed_text)
print(max_length)
min_length = int(max_length/2)

# bart_summarizer = create_bart_summarizer()
# mt5_summarizer = create_mt5_summarizer()
t5_summarizer = create_t5_summarizer()
# pegasus_summarizer = create_pegasus_summarizer()

# print(concat_summaries(mt5_summarizer(raw_text,max_length=max_length, min_length=min_length, do_sample=False)))
# print(concat_summaries(bart_summarizer(processed_text, max_length=max_length, min_length=min_length,do_sample=False)))
print(concat_summaries(t5_summarizer(processed_text,max_length=max_length, min_length=min_length, do_sample=False)))
