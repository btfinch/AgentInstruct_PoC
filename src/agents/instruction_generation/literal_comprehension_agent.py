import json
from ..base_agent import BaseAgent

class LiteralComprehensionAgent(BaseAgent):
    def __init__(self, api_key):
        system_message = """You are an AI assistant that generates literal comprehension questions."""
        super().__init__("LiteralComprehensionAgent", system_message, api_key)

    def generate_response(self, text):
        prompt = f"""
        Generate a literal comprehension question based on the following text:

        {text}

        The question should:
         1. Ask for explicit information directly stated in the text
         2. Be answerable using only the information provided
         3. Be clear and concise

        Format the output as a JSON object with the following structure:
        {{
            "question": "Your generated question",
            "answer": "The correct answer, found explicitly in the text"
        }}
        Ensure the JSON is properly formatted and can be parsed.
        """
        response = super().generate_response(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to generate valid JSON", "raw_response": response}