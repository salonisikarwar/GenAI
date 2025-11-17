import os
from dotenv import load_dotenv
from groq import Groq  # <-- 1. Change import

load_dotenv()
# <-- 2. Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def write_draft(topic: str, outline: str) -> str:
    prompt = f"""
    You are a professional content writer. Based on the topic and outline below, write a full-length content draft.
    
    Make the tone engaging and informative. Add transitions and make sure it flows well.

    Topic: {topic}

    Outline:
    {outline}

    Begin writing:
    """

    try:
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",  # <-- 3. Change model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1200
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"[Error] {str(e)}"