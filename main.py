from dotenv import load_dotenv 
from google import genai


load_dotenv()

client = genai.Client()

def chat_with_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )

    return response.text

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        response = chat_with_gemini(user_input)
        print("Chatbot: ", response)
