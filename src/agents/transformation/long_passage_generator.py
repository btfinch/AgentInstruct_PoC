from ..base_agent import BaseAgent

class LongPassageGenerator(BaseAgent):
    def __init__(self, api_key):
        system_message = """You are an AI assistant that transforms text into longer, narrative-driven passages."""
        super().__init__("LongPassageGenerator", system_message, api_key)

    def generate_response(self, text):
        prompt = f"""
        Expand the following text into a longer, narrative-driven passage:

        {text}

        The expanded passage should:
        1. Be at least 3 paragraphs long
        2. Include descriptive details and context
        3. Maintain a coherent narrative flow
        4. Be suitable for generating comprehension questions
        """
        return super().generate_response(prompt)