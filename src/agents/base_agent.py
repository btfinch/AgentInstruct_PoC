from openai import OpenAI

class BaseAgent:
    def __init__(self, name, system_message, api_key):
        self.name = name
        self._custom_system_message = system_message
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, prompt):
        messages = [
            {"role": "system", "content": self._custom_system_message},
            {"role": "user", "content": prompt}
        ]
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()