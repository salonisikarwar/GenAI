import os
from dotenv import load_dotenv
from langchain.tools import tool
from groq import Groq  # <-- Correct: Using Groq

load_dotenv()
# <-- Correct: Initializing Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@tool
def research_tool(topic: str) -> str:
    """Research a topic and return detailed background information."""
    prompt = f"""
    You are a research assistant. Provide a detailed overview of the topic: "{topic}".
    Include current trends, background, and important points to include in a blog or content.
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # <-- UPDATED
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()

@tool
def outline_tool(topic: str, context: str) -> str:
    """Generate a detailed outline based on topic and research."""
    prompt = f"""
    You are a content strategist. Based on the topic and context, generate a detailed outline.

    Topic: {topic}
    Context: {context}

    Include: intro, 4–6 sections with bullet points, and a conclusion.
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # <-- UPDATED
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()


@tool
def writer_tool(topic: str, outline: str) -> str:
    """Generate a content draft from an outline and topic."""
    prompt = f"""
    You are a professional content writer. Based on the topic and outline below, write a full-length content draft.

    Topic: {topic}
    Outline: {outline}

    Make the tone engaging and informative. Add transitions and ensure it flows well.
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # <-- UPDATED
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content.strip()

@tool
def editor_tool(draft: str, tone: str = "Professional") -> str:
    """Edit the draft for grammar, SEO, and desired tone."""
    prompt = f"""
    You are a content editor. Improve the following content by:
    - Fixing grammar and punctuation
    - Enhancing readability and SEO
    - Making it more {tone.lower()} in tone

    Draft:
    {draft}

    Return the polished version.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # <-- UPDATED
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=1000
    )
    return response.choices[0].message.content.strip()

@tool
def seo_tool(content: str) -> str:
    """Extract 5–10 SEO keywords from the final content."""
    prompt = f"""
    You are an SEO specialist. Analyze the following content and extract the top 5–10 keywords or phrases
    that would help this content rank well in search engines.

    Content:
    {content}

    Return the keywords as a comma-separated list.
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # <-- UPDATED
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=200
    )
    return response.choices[0].message.content.strip()