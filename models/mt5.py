from transformers import pipeline
from transformers import MT5Tokenizer, MT5ForConditionalGeneration

model_name = "mt5-small"

def create_t5_tokenizer():
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    return tokenizer

def create_mt5_summarizer():
    tokenizer = create_bart_tokenizer()
    model = MT5ForConditionalGeneration.from_pretrained(model_name)
    t5_summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    return t5_summarizer
