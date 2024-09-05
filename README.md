# AgentInstruct PoC for Reading Comprehension Skill Fine-Tuning

This project implements a Proof of Concept (PoC) for generating a dataset for fine-tuning language models on reading comprehension tasks using the AgentInstruct framework and the WikiText-103 dataset.

## Setup and Usage

1. Clone the repository:
   ```
   git clone https://github.com/btfinch/AgentInstruct_PoC.git
   cd AgentInstruct_PoC
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the project and its dependencies:
   ```
   pip install -e .
   pip install --upgrade pyautogen
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

5. Run the main script:
   ```
   python main.py
   ```

   Note: On first run, this will download and preprocess the WikiText-103 dataset, which may take some time. Subsequent runs will use the cached preprocessed data.

## Notes

The generated `qa_pairs_for_finetuning.json` file contains additional data used for debugging. The "original_passage" field in this file is not the actual original passage from the dataset.