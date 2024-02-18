# Bachelor Thesis - Computer Science

## Exploring Open Source Generative AI Models for Document Summarization
[![Generic badge](https://img.shields.io/badge/STATUS-IN_PROGRESS-yellow.svg)](https://shields.io/)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Table of Contents

1. [About](#about)
2. [Getting Started](#getting-started)
3. [Project Details](#project-details)
4. [Training Results](#training-results)

## About 
This project explores the potential of open-source generative AI models, particularly those based on the Transformer architecture, for automating the summarization of document content. The goal is to evaluate and apply existing generative AI models to analyze, understand context, and generate summaries for unstructured documents. 


To achieve this, I have fine-tuned two prominent models: [t5-small](https://huggingface.co/t5-small) and [facebook/bart-base](https://huggingface.co/facebook/bart-base), focusing on enhancing their summarization performance.

The focus is on encoder-decoder models following the architecture proposed by the original Transformers due to the complex mapping between input and output sequences required for text summarization. Encoder-decoder models are adept at capturing relationships within these sequences, making them suitable for this task.

![Transformer Architecture](./.github/encoder-decoder.webp)

## Getting Started

Ensure **Python 3.x is installed** on your system. Then, follow the steps below to set up your environment:

### Setup for macOS

```bash
$ xcode-select --install
$ pip3 install --upgrade pip
$ pip3 install --upgrade setuptools
```

### Install Dependencies

```bash
$ pip3 install -r requirements.txt
python3 main.py
```

## Project Details

The project comprises six main phases:

- [x] Extract text from documents
    - [x] PDF
    - [x] DOCX
- [x] Preprocess text
    - [x] Normalize sequences length
    - [x] Tokenizer´s
- [x] Test with different models
    - [x] BART
    - [x] Pegasus
    - [x] T5
    - [x] GPT-2
    - [x] BERT
- [x] Evaluate models performance
    - [x] rouge score
- [x] Choose Dataset for Fine-tuning
- [x] Fine-tune the pre-trained model with best performance
    - [x] T5 [![Open T5 Training in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12JCwt5OXmqJJYXUFHNGXYuiBeneabz-E?usp=sharing)
    - [x] BART [![Open Bart Training in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nG6EjN2E0hAga50aAx4plcP7tpk6zVmc?ouid=116455225505048388373&usp=drive_link)

### Training Data

The dataset used for fine-tuning the T5 and BART models was the [Big Patent Dataset](https://huggingface.co/datasets/big_patent), which is composed of 1.3 million U.S. patent documents along with their human-written abstractive summaries. Each document in this dataset is categorized under a Cooperative Patent Classification (CPC) code, covering a broad range of topics from human necessities to physics and electricity. This diversity ensures that the models encounter a wide variety of language use and technical jargon, which is crucial for developing a robust summarization capability.

The Big Patent Dataset was chosen due to its relevance to the project's goal of summarizing complex documents. Patents are inherently detailed and technical, making them an ideal challenge for testing the models' ability to condense information while preserving the core content and context. The dataset's structured format and the presence of high-quality summaries provide a strong foundation for training and evaluating the models' performance in generating accurate and coherent summaries.

## Training Results

The performance of the models was evaluated using the ROUGE metric, emphasizing their ability to generate summaries closely aligned with human-written abstracts. Both BART and T5 models were fine-tuned using the Big Patent Dataset, focusing on achieving high-quality abstract summarization.

### BART

| **Metric**                              | **Value**  |
|-----------------------------------------|------------|
| Evaluation Loss (Eval Loss)             | 1.9244     |
| Rouge-1                                 | 0.5007     |
| Rouge-2                                 | 0.2704     |
| Rouge-L                                 | 0.3627     |
| Rouge-Lsum                              | 0.3636     |
| Average Generation Length (Gen Len)     | 122.1489   |
| Runtime (seconds)                       | 1459.3826  |
| Samples per Second                      | 1.312      |
| Steps per Second                        | 0.164      |


### T5

| **Metric**                              | **Value** |
|-----------------------------------------|-----------|
| Evaluation Loss (Eval Loss)             | 1.9984    |
| Rouge-1                                 | 0.503     |
| Rouge-2                                 | 0.286     |
| Rouge-L                                 | 0.3813    |
| Rouge-Lsum                              | 0.3813    |
| Average Generation Length (Gen Len)     | 151.918   |
| Runtime (seconds)                       | 714.4344  |
| Samples per Second                      | 2.679     |
| Steps per Second                        | 0.336     |


