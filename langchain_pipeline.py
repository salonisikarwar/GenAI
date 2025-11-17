# agents/langchain_pipeline.py

from agents.langchain_agents import (
    research_tool,
    outline_tool,
    writer_tool,
    editor_tool,
    seo_tool
)
from langchain_core.runnables import RunnableLambda

# Step 1: Research
research_chain = RunnableLambda(lambda x: {
    "topic": x["topic"],
    "context": research_tool.invoke(x["topic"])
})

# Step 2: Outline
outline_chain = RunnableLambda(lambda x: {
    "topic": x["topic"],
    "outline": outline_tool.invoke({
        "topic": x["topic"],
        "context": x["context"]
    })
})

# Step 3: Write Draft
write_chain = RunnableLambda(lambda x: {
    "topic": x["topic"],
    "draft": writer_tool.invoke({
        "topic": x["topic"],
        "outline": x["outline"]
    })
})

# Step 4: Edit with Tone
edit_chain = RunnableLambda(lambda x: {
    "final": editor_tool.invoke({
        "draft": x["draft"],
        "tone": x.get("tone", "Professional")
    })
})

# Step 5: SEO Keywords Extraction
seo_chain = RunnableLambda(lambda x: {
    "final": x["final"],
    "keywords": seo_tool.invoke(x["final"])
})

# Combine the chain
chain = research_chain | outline_chain | write_chain | edit_chain | seo_chain








