from ..base_agent import BaseAgent

class DebateGenerator(BaseAgent):
    def __init__(self, api_key):
        system_message = """You are an AI assistant that transforms text into a debate format."""
        super().__init__("DebateGenerator", system_message, api_key)

    def generate_response(self, text):
        prompt = f"""
        Transform the following text into a debate format with opposing viewpoints:

        {text}

        Format the output as follows:
        Topic: [Main topic of debate]
        
        Perspective 1:
        - Argument 1: [First argument supporting this perspective]
        - Argument 2: [Second argument supporting this perspective]
        
        Perspective 2:
        - Counterargument 1: [First argument opposing Perspective 1]
        - Counterargument 2: [Second argument opposing Perspective 1]
        
        Conclusion: [A balanced summary of the debate]
        """
        return super().generate_response(prompt)