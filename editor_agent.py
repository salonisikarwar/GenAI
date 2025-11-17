import os
from dotenv import load_dotenv
from groq import Groq  # <-- 1. Change import

load_dotenv()
# <-- 2. Initialize Groq client using GROQ_API_KEY
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def edit_content(draft: str) -> str:
    prompt = f"""
    You are a professional content editor. Take the following draft and improve it by:
    - Fixing grammar and punctuation
    - Improving readability and tone
    - Making it more engaging and conversational
    - Enhancing SEO (without keyword stuffing)
    - Keeping structure intact

    Draft:
    {draft}

    Return the polished version.
    """

    try:
        response = client.chat.completions.create(
            # <-- 3. Change model to a Groq model
            model="mixtral-8x7b-32768", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=1200
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"[Error] {str(e)}"