from datasets import load_dataset, load_metric
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import numpy as np
import random
import torch

dataset = load_dataset("samsum")

rouge = load_metric("rouge")

model_names = {
    "T5": "t5-small",
    "BART": "facebook/bart-base",
}

percentage = 0.1
sample_size = int(len(dataset["test"]) * percentage)
sampled_indices = random.sample(range(len(dataset["test"])), sample_size)
sampled_dataset = dataset["test"].select(sampled_indices)

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    result = rouge.compute(predictions=decoded_preds, references=decoded_labels, use_stemmer=True)
    prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in predictions]
    
    final_result = {metric: scores.mid.fmeasure for metric, scores in result.items()}
    final_result["gen_len"] = np.mean(prediction_lens)
    return final_result

def evaluate_model(model_name, tokenizer, model, dataset):
    summaries = []
    references = []

    for example in dataset:
        inputs = tokenizer(example["dialogue"], return_tensors="pt", max_length=1024, truncation=True)

        summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        summaries.append(summary)
        references.append(example["summary"])

    eval_pred = (torch.tensor(tokenizer(summaries, padding=True, truncation=True)["input_ids"]),
                 torch.tensor(tokenizer(references, padding=True, truncation=True)["input_ids"]))
    
    result = compute_metrics(eval_pred)
    return result

for model_name, model_path in model_names.items():
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    result = evaluate_model(model_name, tokenizer, model, sampled_dataset)
    print(f"Resultados para {model_name}: {result}")
