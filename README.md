# AgentInstruct PoC for Reading Comprehension Skill Fine-Tuning

This project implements a Proof of Concept (PoC) for generating a dataset for fine-tuning language models on reading comprehension tasks using the AgentInstruct framework and the WikiText-103 dataset.

## Project Structure

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your OpenAI API key in a `.env` file
4. Generate the preprocessed paragraphs:
   ```
   python -c "from src.utils.data_utils import load_wikitext_103, get_preprocessed_paragraphs; dataset = load_wikitext_103(); get_preprocessed_paragraphs(dataset)"
   ```
   This will create a `data/preprocessed_paragraphs.pkl` file.

## Usage

Run the main script:

## Notes:

Right now if you run this and generate qa_pairs_for_finetuning.json it outputs a lot of data that I'm using for debugging. Note the original passage here is not the original passage