import os
from dotenv import load_dotenv
from groq import Groq  # <-- 1. Change import

load_dotenv()
# <-- 2. Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def research_topic(topic: str) -> str:
    prompt = f"""
    You are a research assistant. Provide a detailed overview of the topic: "{topic}".
    Include current trends, background, and important points to include in a blog or content.
    Make it factual and helpful for content creation.
    """

    try:
        response = client.chat.completions.create(
            # <-- 3. Change model to a Groq model
            model="mixtral-8x7b-32768", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=700
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"[Error] {str(e)}"


if __name__ == '__main__':
    topic_summary  = research_topic("generative ai")
    print(topic_summary)