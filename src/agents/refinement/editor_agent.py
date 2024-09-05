from ..base_agent import BaseAgent
import json

class EditorAgent(BaseAgent):
    def __init__(self, api_key):
        system_message = """You are an AI assistant that refines and improves questions based on strategic suggestions."""
        super().__init__("EditorAgent", system_message, api_key)

    def generate_response(self, passage, question, answer, strategy_suggestions):
        prompt = f"""
        Refine the following passage, question, and answer based on the provided strategy suggestions:

        Original Passage: {passage}
        Original Question: {question}
        Original Answer: {answer}

        Strategy Suggestions:
        {strategy_suggestions}

        Implement the most effective strategy to create a more challenging question-answer pair. Ensure that the refinement aligns with one of these goals:
        1. Make the question unanswerable by modifying the passage
        2. Alter the answer by modifying the passage
        3. Increase the complexity of the question or answer choices

        Format your response as a JSON object with the following structure:
        {{
            "passage": "Your modified version of the passage (if applicable)",
            "question": "Your improved version of the question",
            "answer": "The correct answer to the refined question"
        }}
        Ensure the JSON is properly formatted and can be parsed.
        """
        response = super().generate_response(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to generate valid JSON", "raw_response": response}