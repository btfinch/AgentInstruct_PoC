from datasets import load_dataset
import re
import pickle
import os

def load_wikitext_103():
    """
    Load the WikiText-103 dataset.
    """
    return load_dataset("wikitext", "wikitext-103-raw-v1")

def preprocess_text(text):
    """
    Preprocess the text by removing special tokens and extra whitespace.
    """
    # Remove special tokens
    text = re.sub(r'=+\s*[^=]+\s*=+', '', text)  # Remove section headers
    text = re.sub(r'@-@', '-', text)  # Replace @-@ with -
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def split_into_paragraphs(text):
    """
    Split the text into paragraphs.
    """
    return [p.strip() for p in text.split('\n\n') if p.strip()]

def get_preprocessed_paragraphs(dataset, split='train', min_length=100, cache_file='data/preprocessed_paragraphs.pkl'):
    cache_dir = os.path.dirname(cache_file)
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    
    if os.path.exists(cache_file):
        print("Loading preprocessed paragraphs from cache...")
        with open(cache_file, 'rb') as f:
            return pickle.load(f)
    
    print("Preprocessing paragraphs...")
    preprocessed_paragraphs = []
    
    for item in dataset[split]:
        text = preprocess_text(item['text'])
        paragraphs = split_into_paragraphs(text)
        
        for paragraph in paragraphs:
            if len(paragraph) >= min_length:
                preprocessed_paragraphs.append(paragraph)
    
    print("Saving preprocessed paragraphs to cache...")
    with open(cache_file, 'wb') as f:
        pickle.dump(preprocessed_paragraphs, f)
    
    return preprocessed_paragraphs

# Example usage
if __name__ == "__main__":
    dataset = load_wikitext_103()
    paragraphs = get_preprocessed_paragraphs(dataset)
    print(f"Total preprocessed paragraphs: {len(paragraphs)}")
    print("Sample paragraph:")
    print(paragraphs[0])