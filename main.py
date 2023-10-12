# from PyPDF2 import PdfReader
from pypdf import PdfReader

from models.bart import create_bart_summarizer

def extract_text(filename, max_length_sequence):
    reader = PdfReader('./resource/inputs/' + filename)
    extracted_text = []

    for page in reader.pages:
        text = page.extract_text()
        extracted_text.append(text)

    segments = []
    for text in extracted_text:
        for i in range(0, len(text), max_length_sequence):
            segment = text[i:i + max_length_sequence]
            segments.append(segment)

    return segments

text = extract_text('once-upon-a-time-test.pdf', 1024)
bart_summarizer = create_bart_summarizer()


print(bart_summarizer(text, max_length=130, min_length=30, do_sample=False))
