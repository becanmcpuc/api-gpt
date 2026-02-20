from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class GPT:
    client = OpenAI()

    def __init__(self, model: str):
        self.model = model

    def ask(self, text: str):
        response = self.client.responses.create(
            model=self.model,
            input=text
        )

        return response.output_text