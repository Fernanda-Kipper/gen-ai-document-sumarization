from transformers import logging

from pypdf import PdfReader
import docx
from simplify_docx import simplify

from models.bart import create_bart_summarizer
from models.t5.summarizer import create_t5_summarizer, create_t5_tokenizer

logging.set_verbosity_error()

def break_text_in_sequences1(extracted_text,max_length_sequence):
    segments = []
    for text in extracted_text:
        text = text.replace("\n", " ")
        for i in range(0, len(text), max_length_sequence):
            segment = text[i:i + max_length_sequence]
            segments.append(segment)
    return segments

def break_text_in_sequences(tokenizer, text, max_length_sequence):
    # Divide o texto em palavras
    words = text.split()
    current_chunk = 1
    chunks = ['']
    
    for word in words:
        # Testa se o comprimento do chunk atual com a nova palavra excede o limite máximo
        if len(tokenizer.encode(chunks[current_chunk - 1] + ' ' + word, add_special_tokens=True)) > max_length_sequence:
            # Começa um novo chunk
            current_chunk += 1
            chunks.append(word)
        else:
            # Adiciona a palavra ao chunk atual
            chunks[current_chunk - 1] += ' ' + word

    # Remove o espaço inicial de cada chunk
    chunks = [chunk.strip() for chunk in chunks]
    return chunks

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

def concat_summaries(summarizer, text_segments):
    final_summary = ""
    for segment in text_segments:
        input_length = len(segment.split())  # Número de palavras no segmento de texto
        max_length = min(150, int(input_length * 0.6))  # max_length como 60% do input_length ou 150, o que for menor
        min_length = max(5, int(max_length * 0.5))  # min_length como 50% do max_length
        
        summary = summarizer(segment, max_length=max_length, min_length=min_length, do_sample=False)
        final_summary += summary[0]['summary_text']
    return final_summary

def calculate_max_length_of_summary(text_list):
    min_text_length = 1024
    for text in text_list:
        if(len(text.strip()) < min_text_length):
            min_text_length = len(text.strip())
    return int(min_text_length/2)

# raw_text = extract_text_from_pdf('transformers.pdf')
tokenizer = create_t5_tokenizer()
raw_text = " ".join(extract_text_from_docx('once-upon-a-time-test.docx'))
processed_text = break_text_in_sequences(tokenizer, raw_text, 1024)

# bart_summarizer = create_bart_summarizer()
t5_summarizer = create_t5_summarizer()

# print(concat_summaries(bart_summarizer, processed_text))
print(concat_summaries(t5_summarizer, processed_text))