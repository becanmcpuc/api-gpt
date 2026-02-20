import os, sys
SERVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),"../.."))
sys.path.append(SERVER_PATH)

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

from src.models.message import Message

class GPT:
    def __init__(self, model: str):
        self.client = OpenAI()
        self.model: str = model
        self.history: list[dict] = []

    def __add_message_to_history(self, role: str, message: str):
        self.history.append(
            Message(
                role=role, 
                message=message
            ).make_buffer()
        )

    def ask(self, text: str):

        self.__add_message_to_history(role='user', message=text)

        response = self.client.responses.create(
            model=self.model,
            input=f'{self.history}'
        )

        self.__add_message_to_history(role='assistent', message=response)

        return response.output_text