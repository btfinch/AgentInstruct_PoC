import pickle
import os
from datasets import load_dataset

def load_or_create_preprocessed_paragraphs(file_path='data/preprocessed_paragraphs.pkl', min_length=100):
    if os.path.exists(file_path):
        print("Loading preprocessed paragraphs from cache...")
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    
    print("Preprocessing paragraphs...")
    dataset = load_dataset("wikitext", "wikitext-103-raw-v1", split="train")
    paragraphs = [p for p in dataset["text"] if len(p.split()) >= min_length]
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        pickle.dump(paragraphs, f)
    
    return paragraphs

def get_preprocessed_paragraphs():
    return load_or_create_preprocessed_paragraphs()

# Remove the load_wikitext_103 function as it's no longer needed