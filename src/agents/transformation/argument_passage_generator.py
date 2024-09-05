from ..base_agent import BaseAgent

class ArgumentPassageGenerator(BaseAgent):
    def __init__(self, api_key):
        system_message = """You are an AI assistant that transforms text into structured argument passages.
        When given a text, you will transform it into a passage with clear claims and supporting evidence."""
        super().__init__("ArgumentPassageGenerator", system_message, api_key)

    def generate_response(self, text):
        prompt = f"""
        Transform the following text into a structured argument passage with claims and evidence:

        {text}

        Format the output as follows:
        Claim 1: [Main claim]
        Evidence: [Supporting evidence]
        Claim 2: [Secondary claim]
        Evidence: [Supporting evidence]
        ...
        """
        return super().generate_response(prompt)