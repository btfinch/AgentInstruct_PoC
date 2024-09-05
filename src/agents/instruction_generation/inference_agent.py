import json
from ..base_agent import BaseAgent

class InferenceAgent(BaseAgent):
    def __init__(self, api_key):
        system_message = """You are an AI assistant that generates inference questions."""
        super().__init__("InferenceAgent", system_message, api_key)

    def generate_response(self, text):
        prompt = f"""
        Generate an inference question based on the following text:

        {text}

        The question should:
        1. Require the reader to draw conclusions or make predictions not explicitly stated in the text
        2. Be answerable by combining information from the text with general knowledge
        3. Encourage critical thinking

        Format the output as a JSON object with the following structure:
        {{
            "question": "Your generated inference question",
            "answer": "The correct answer, based on reasonable inference from the text"
        }}
        Ensure the JSON is properly formatted and can be parsed.
        """
        response = super().generate_response(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to generate valid JSON", "raw_response": response}