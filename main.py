
from PyPDF2 import PdfReader
from transformers import pipeline

reader = PdfReader('./inputs/gans.pdf')
  
print(len(reader.pages))
  
page = reader.pages[0]

text = page.extract_text()

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

print(summarizer(text, max_length=130, min_length=30, do_sample=False))