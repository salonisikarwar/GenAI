import os
from dotenv import load_dotenv
from groq import Groq  # <-- 1. Change import

load_dotenv()
# <-- 2. Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_outline(topic: str, context: str) -> str:
    prompt = f"""
    You are a content strategist. Based on the following topic and context, generate a detailed outline for a blog or script.

    Topic: {topic}

    Context:
    {context}

    Your outline should have:
    - Introduction
    - 4 to 6 major sections with headings
    - Bullet points under each section
    - A conclusion

    Make it clean and well-structured.
    """

    try:
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",  # <-- 3. Change model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=800
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"[Error] {str(e)}"