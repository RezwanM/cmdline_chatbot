import os
from dotenv import load_dotenv
from google import genai
from rich.console import Console
from rich.markdown import Markdown


load_dotenv()

client = genai.Client()


def chat_with_gemini(prompt: str) -> str:
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text

def main():
    console = Console()
    right_pad = "\x1b[0m"
    user_left_pad = "\x1b[36m"
    chatbot_left_pad = "\x1b[33m"

    print("Welcome to the AI Chatbot (powered by Gemini)!\n")
    print("Start by entering a prompt.")
    print('(For quitting the application, type "quit".)')
    print('(For clearing the screen, type "clear".)\n')

    while True:
        user_input = input(user_left_pad + "You: " + right_pad)
        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "clear":
            os.system("cls" if os.name == "nt" else "clear")
        else:
            response = chat_with_gemini(user_input)
            markdown = Markdown(response)
            print(chatbot_left_pad + "Chatbot: " + right_pad)
            console.print(markdown)
    print("\nThank you for using the AI Chatbot. Until next time!")

if __name__ == "__main__":
    main()
