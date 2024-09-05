import json
from ..base_agent import BaseAgent

class StrengthenWeakenAgent(BaseAgent):
    def __init__(self, api_key):
        system_message = """You are an AI assistant that generates strengthen/weaken questions."""
        super().__init__("StrengthenWeakenAgent", system_message, api_key)

    def generate_response(self, text):
        prompt = f"""
        Generate a strengthen/weaken question based on the following text:

        {text}

        The question should:
        1. Identify a key argument or claim in the text
        2. Ask the reader to choose a statement that either strengthens or weakens this argument
        3. Provide multiple choice options, including the correct answer and plausible distractors

        Format the output as a JSON object with the following structure:
        {{
            "question": "Which of the following, if true, would [strengthen/weaken] the argument that [key argument]?",
            "answer": "The correct answer option (A, B, C, or D)",
            "options": {{
                "A": "Option that strengthens/weakens the argument",
                "B": "Distractor option",
                "C": "Distractor option",
                "D": "Distractor option"
            }}
        }}
        Ensure the JSON is properly formatted and can be parsed.
        """
        response = super().generate_response(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to generate valid JSON", "raw_response": response}