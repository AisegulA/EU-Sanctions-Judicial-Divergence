# text_processing.py
# Sample script for processing legal texts using SpaCy

import spacy
from pathlib import Path

nlp = spacy.load("en_core_web_sm")

def process_text(file_path):
    text = Path(file_path).read_text()
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

# Example usage
# print(process_text("sample.txt"))
