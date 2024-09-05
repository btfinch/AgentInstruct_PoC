import os
import json
import random
import logging
from dotenv import load_dotenv
from src.utils.data_utils import get_preprocessed_paragraphs
from src.agents.transformation import ArgumentPassageGenerator, LongPassageGenerator, DebateGenerator
from src.agents.instruction_generation import (
    LiteralComprehensionAgent, InferenceAgent, StrengthenWeakenAgent,
    SummarizationAgent, ReasoningAgent
)
from src.agents.refinement import SuggesterAgent, EditorAgent
from src.utils.evaluation_metrics import evaluate_dataset

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

def process_paragraph(paragraph, transform_agent, instruction_agents, suggester_agent, editor_agent):
    qa_pairs = []
    try:
        logging.info(f"Transforming with {transform_agent.name}...")
        transformed_passage = transform_agent.generate_response(f"Transform this text: {paragraph}")
        
        for instruction_agent in instruction_agents:
            try:
                logging.info(f"Generating question with {instruction_agent.name}...")
                original_qa = instruction_agent.generate_response(f"Generate a question for this text: {transformed_passage}")
                
                if isinstance(original_qa, dict) and "question" in original_qa and "answer" in original_qa:
                    original_question = original_qa["question"]
                    original_answer = original_qa["answer"]
                    
                    logging.info("Suggesting refinement strategies...")
                    strategy_suggestions = suggester_agent.generate_response(transformed_passage, original_question, original_answer)
                    
                    logging.info("Refining question...")
                    edited_qa = editor_agent.generate_response(transformed_passage, original_question, original_answer, strategy_suggestions)
                    
                    if "error" not in edited_qa:
                        qa_pairs.append({
                            "original_passage": transformed_passage,
                            "original_question": original_question,
                            "original_answer": original_answer,
                            "passage": edited_qa.get("passage", transformed_passage),
                            "question": edited_qa["question"],
                            "answer": edited_qa["answer"],
                            "instruction_agent": instruction_agent.name,
                            "transformation_agent": transform_agent.name
                        })
                    else:
                        logging.error(f"Error in refining question: {edited_qa['error']}")
                else:
                    logging.error(f"Invalid response from {instruction_agent.name}: {original_qa}")
            except Exception as e:
                logging.error(f"Error in instruction generation: {str(e)}")
    except Exception as e:
        logging.error(f"Error in transformation: {str(e)}")
    
    return qa_pairs

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in the .env file")

    logging.info("Loading or creating preprocessed paragraphs...")
    paragraphs = get_preprocessed_paragraphs()
    logging.info(f"Total preprocessed paragraphs: {len(paragraphs)}")

    # Initialize agents
    transformation_agents = [
        ArgumentPassageGenerator(api_key),
        LongPassageGenerator(api_key),
        DebateGenerator(api_key)
    ]
    instruction_agents = [
        LiteralComprehensionAgent(api_key),
        InferenceAgent(api_key),
        StrengthenWeakenAgent(api_key),
        SummarizationAgent(api_key),
        ReasoningAgent(api_key)
    ]
    suggester_agent = SuggesterAgent(api_key)
    editor_agent = EditorAgent(api_key)

    # Process multiple paragraphs
    num_paragraphs_to_process = 2  # Adjust this number as needed
    selected_paragraphs = random.sample(paragraphs, num_paragraphs_to_process)
    
    all_qa_pairs = []
    for i, paragraph in enumerate(selected_paragraphs):
        logging.info(f"Processing paragraph {i+1}/{num_paragraphs_to_process}")
        # Randomly select one transformation agent for each paragraph
        transform_agent = random.choice(transformation_agents)
        qa_pairs = process_paragraph(paragraph, transform_agent, instruction_agents, suggester_agent, editor_agent)
        all_qa_pairs.extend(qa_pairs)

    if all_qa_pairs:
        # Evaluate the dataset
        evaluation_results = evaluate_dataset(all_qa_pairs)
        logging.info("Dataset evaluation results:")
        for metric, value in evaluation_results.items():
            logging.info(f"{metric}: {value}")

        # Save all QA pairs to a JSON file
        output_file = 'qa_pairs_for_finetuning.json'
        with open(output_file, 'w') as f:
            json.dump(all_qa_pairs, f, indent=2)

        # Save evaluation results
        with open('evaluation_results.json', 'w') as f:
            json.dump(evaluation_results, f, indent=2)

        logging.info(f"Generated {len(all_qa_pairs)} QA pairs for fine-tuning.")
        logging.info(f"QA pairs saved to '{output_file}'")
    else:
        logging.warning("No valid QA pairs were generated. Check the logs for errors.")

    logging.info("Script completed successfully.")

if __name__ == "__main__":
    main()
