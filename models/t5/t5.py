from transformers import pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = "t5-small"

def create_t5_tokenizer():
    tokenizer = T5Tokenizer.from_pretrained(model_name, padding='max-length', truncation=True, legacy=False)
    return tokenizer

def create_t5_summarizer():
    tokenizer = create_t5_tokenizer()
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    t5_summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    return t5_summarizer
