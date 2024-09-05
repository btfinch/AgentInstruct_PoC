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

## Running the Web Interface

After setting up the project, you can run the web interface:

1. Ensure you're in the project root directory and your virtual environment is activated.

2. Run the Flask app:
   ```
   python app.py
   ```

3. Open a web browser and go to `http://127.0.0.1:5000/`

This will launch a simple web interface where you can interact with the various agents and see how they process the data.

## Using the Web Interface

The web interface allows you to interact with the AgentInstruct PoC system. Here's how to use it:

1. **Get Random Paragraph**: Click this button to fetch a random paragraph from the preprocessed dataset.

2. **Transformation**:
   - Select a transformation agent from the dropdown menu.
   - Click "Transform" to apply the selected transformation to the paragraph.

3. **Instruction Generation**:
   - Select an instruction generation agent from the dropdown menu.
   - Click "Generate Instruction" to create a question-answer pair based on the transformed text.

4. **Suggestion**:
   - After generating an instruction, click "Get Suggestion" to receive suggestions on how to make the question more challenging.

5. **Edit**:
   - Once you have a suggestion, click "Edit QA Pair" to see the final refined question-answer pair.

Each step's output will be displayed in the interface, allowing you to see how the text is processed and refined through the AgentInstruct pipeline.

## Notes

- The generated `qa_pairs_for_finetuning.json` file contains additional data used for debugging. The "original_passage" field in this file is not the actual original passage from the dataset.
- The web interface is for demonstration purposes and processes one paragraph at a time. For bulk processing, use the `main.py` script.