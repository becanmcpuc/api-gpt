import os, sys
SERVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),"../.."))
sys.path.append(SERVER_PATH)

from openai import OpenAI
from src.models.openai import GPT

def create_model():
    gpt = GPT("gpt-4.1")
    return gpt

def test_ask():
    gpt = create_model()

    response = gpt.ask(30)

    print(response)

test_ask()
