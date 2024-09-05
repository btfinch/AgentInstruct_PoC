from openai import OpenAI
from autogen import AssistantAgent

class BaseAgent(AssistantAgent):
    def __init__(self, name, system_message, api_key):
        super().__init__(name=name, system_message=system_message)
        self._custom_system_message = system_message
        self.client = OpenAI(api_key=api_key)

    async def a_generate(self, messages, sender, config):
        human_message = messages[-1]["content"]
        response = self.generate_response(human_message)
        return {"content": response}

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