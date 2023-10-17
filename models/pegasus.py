from transformers import pipeline
from transformers import PegasusTokenizer, PegasusForConditionalGeneration

model_name = "google/pegasus-xsum"

def create_pegasus_tokenizer():
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    return tokenizer

def create_pegasus_summarizer():
    tokenizer = create_pegasus_tokenizer()
    model = PegasusForConditionalGeneration.from_pretrained(model_name)
    pegasus_summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    return pegasus_summarizer