import json
from ..base_agent import BaseAgent

class ReasoningAgent(BaseAgent):
    def __init__(self, api_key):
        system_message = """You are an AI assistant that generates reasoning questions."""
        super().__init__("ReasoningAgent", system_message, api_key)

    def generate_response(self, text):
        prompt = f"""
        Generate a reasoning question based on the following text:

        {text}

        The question should:
        1. Test the reader's ability to follow logical arguments presented in the text
        2. Require analysis of the relationships between different ideas in the passage
        3. Encourage critical evaluation of the author's reasoning or methodology

        Format the output as a JSON object with the following structure:
        {{
            "question": "Your generated reasoning question",
            "answer": "The correct answer, demonstrating sound reasoning based on the text",
            "explanation": "Brief explanation of the logical steps or critical thinking required to arrive at the answer"
        }}
        Ensure the JSON is properly formatted and can be parsed.
        """
        response = super().generate_response(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to generate valid JSON", "raw_response": response}