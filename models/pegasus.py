from transformers import pipeline
from transformers import AutoTokenizer

def create_generic_tokenizer():
    checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    return tokenizer

def create_pegasus_summarizer():
    tokenizer = create_generic_tokenizer()
    pegasus_summarizer = pipeline("summarization", model="google/pegasus-xsum")
    return pegasus_summarizer