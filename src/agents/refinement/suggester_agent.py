from ..base_agent import BaseAgent

class SuggesterAgent(BaseAgent):
    def __init__(self, api_key):
        system_message = """You are an AI assistant that suggests strategies to make questions more complex or challenging."""
        super().__init__("SuggesterAgent", system_message, api_key)

    def generate_response(self, passage, question, answer):
        prompt = f"""
        Analyze the following passage, question, and answer. Suggest strategies to make the question more challenging or complex using one of these three approaches:

        1. Strategy to make the question unanswerable
        2. Strategy to alter the answer, if possible, in the opposite direction
        3. Strategy to increase the complexity of the question or answer choices

        Passage: {passage}
        Question: {question}
        Answer: {answer}

        For each approach, provide a strategy suggestion:
        1. Unanswerable strategy: [Your suggestion for making the question unanswerable]
        2. Answer alteration strategy: [Your suggestion for changing the answer]
        3. Complexity increase strategy: [Your suggestion for making the question more complex]

        Choose the most effective strategy and explain why it would be most challenging.
        Do not provide specific edits or modifications, only strategic suggestions.
        """
        return super().generate_response(prompt)