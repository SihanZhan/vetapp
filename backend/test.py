from openai import OpenAI
from dotenv import load_dotenv
import os 
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")


system_prompt = {"role": "system", "content": "You are VetAI, a highly knowledgeable and helpful veterinary assistant. "
        "You provide clear, professional, and accurate advice about pet health, "
        "behavior, and general care for cats, dogs, and other common household pets. "
        "Always prioritize animal safety and welfare. "
        "If the user asks about serious symptoms, advise them to visit a veterinarian immediately. "
        "Your tone should be friendly, empathetic, and easy to understand, avoiding medical jargon unless necessary. "
        "You can provide general guidance, tips, and educational information, "
        "but you never replace a real veterinarian." }
while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "exit":
        print("Goodbye!")
        break
    messages = [system_prompt, {"role": "user", "content": user_input}]
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=False
    )
    print("AI:", response.choices[0].message.content)