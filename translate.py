import os
from openai import OpenAI
from dotenv import load_dotenv
from langdetect import detect

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def translate_to_english(text):
    language = detect(text)

    if language == "en":
        return text

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": f"Translate this to English: {text}"}
        ]
    )

    return response.choices[0].message.content