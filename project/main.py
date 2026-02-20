from src.models.openai import GPT
from src.utils.colorama_utils import color

def main():
    gpt = GPT("gpt-4.1")

    while True:
        text = input(color("> ", "RED"))
        response = gpt.ask(text)
        print(color(response, "GREEN"))

if __name__ == "__main__":
    main()