import json
from ..base_agent import BaseAgent

class SummarizationAgent(BaseAgent):
    def __init__(self, api_key):
        system_message = """You are an AI assistant that generates summarization questions."""
        super().__init__("SummarizationAgent", system_message, api_key)

    def generate_response(self, text):
        prompt = f"""
        Generate a summarization question based on the following text:

        {text}

        The question should:
        1. Ask the reader to provide a concise summary of the main points in the text
        2. Encourage the identification of key ideas and themes
        3. Require the reader to distill the essence of the passage in their own words

        Format the output as a JSON object with the following structure:
        {{
            "question": "Summarize the main points of the given text in 2-3 sentences.",
            "answer": "A concise summary that captures the main ideas of the text",
            "key_points": [
                "Key point 1",
                "Key point 2",
                "Key point 3"
            ]
        }}
        Ensure the JSON is properly formatted and can be parsed.
        """
        response = super().generate_response(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to generate valid JSON", "raw_response": response}