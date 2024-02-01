from transformers import pipeline
from transformers import BartTokenizer, BartForConditionalGeneration

model_name = "facebook/bart-large-cnn"

def create_bart_tokenizer():
    tokenizer = BartTokenizer.from_pretrained(model_name, padding='max-length', truncation=True)
    return tokenizer

def create_bart_summarizer():
    tokenizer = create_bart_tokenizer()
    model = BartForConditionalGeneration.from_pretrained(model_name)
    bart_summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    return bart_summarizer
