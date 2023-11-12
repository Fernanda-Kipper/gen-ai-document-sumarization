# Bachelor Thesis - Computer Science

## Exploring Open Source Generative AI models for understanding and summarizing documents

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

[![Generic badge](https://img.shields.io/badge/STATUS-WIP-yellow.svg)](https://shields.io/)

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ecrtccypWJBdKKduqjiIvPkgLQwTAyYO?usp=sharing)

The purpose of this work is to explore the potential of generative AIs, in particular those based on the Transformer architecture, to automate the process of summarizing content of documents. The main objective is to study and explore existing open source artificial intelligence (AI) models, with a focus on generative AIs, aiming for the ability to perform analysis, understand context and generate summaries for unstructured documents available on the internet.

For this, we will use encoder-decoder models, following the architecture proposed by the original Transformers (image 1), because text summarization requires a complex mapping between input and output sequences and it is crucial to capture the relationships between elements in both sequences. And encoder-decoder models perform better in this task.

<img src="./.github/encoder-decoder.webp" />


## Work Steps

- [ ] Extract text from documents
    - [x] PDF
    - [x] DOCX
    - [ ] PNG / JPEG
- [x] Preprocess text
    - [x] Normalize sequences length
    - [x] Tokenizer´s
- [ ] Test with different models
    - [x] BART
    - [x] Pegasus
    - [x] T5
    - [x] mT5
    - [ ] mBART
- [ ] Evaluate model performance
    - [ ] rouge score
- [ ] Choose Datasets for Fine-tuning
- [ ] Fine-tune the pretrained model with best performance

## How it Works

> WIP

## How to run

1. You need to have Python V3 installed

2. If you are in MacOs, run the following command

```bash
$ xcode-select --install
$ pip3 install --upgrade pip
$ pip3 install --upgrade setuptools
$ pip3 install requirements.txt
``````

2. Run the following command

```bash
pip3 install
python3 main.py
```

## How to use this work

> WIP
