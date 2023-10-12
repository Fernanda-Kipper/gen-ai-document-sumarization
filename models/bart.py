from transformers import pipeline
from transformers import BartTokenizer, BartForConditionalGeneration

def create_bart_tokenizer():
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    return tokenizer

def create_bart_summarizer():
    tokenizer = create_bart_tokenizer()
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    bart_summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    return bart_summarizer
