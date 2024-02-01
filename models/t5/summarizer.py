from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

model_name = "KipperDev/t5_summarizer_model"

def create_t5_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return tokenizer

def create_t5_summarizer():
    try:
        tokenizer = create_t5_summarizer()
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
        return summarizer

    except Exception as e:
        print(f"Erro ao carregar modelo/tokenizador: {e}")
        raise

