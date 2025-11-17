import os  # <-- 1. Add import
from agents.research_agent import research_topic
from agents.outline_agent import generate_outline
from agents.writer_agent import write_draft
from agents.editor_agent import edit_content
from agents.image_agent import generate_image
from utils.exporter import save_as_markdown, save_as_pdf, EXPORT_DIR  # <-- 2. Import EXPORT_DIR

def main():
    print("🚀 Welcome to AgentX - AI-Powered Content Creator")
    topic = input("🔍 Enter your content topic or brief: ")

    print("\n📚 Researching...")
    background = research_topic(topic)
    print("\n🔎 Background Info:\n", background)

    print("\n🧠 Generating Outline...")
    outline = generate_outline(topic, background)
    print("\n📝 Content Outline:\n", outline)

    print("\n✍️ Writing First Draft...")
    draft = write_draft(topic, outline)
    print("\n📄 Content Draft:\n", draft)

    print("\n🧹 Editing & Optimizing...")
    final_content = edit_content(draft)
    print("\n✅ Final Edited Content:\n", final_content)

    print("\n🖼️ Generating Visual...")
    
    # --- THIS IS THE CHANGED SECTION ---
    
    # 3. Create a unique path for the image in the 'exports' folder
    image_filename = f"{topic.replace(' ', '_').lower()}_image.png"
    image_output_path = os.path.join(EXPORT_DIR, image_filename)
    
    # 4. Call generate_image with the new output path
    image_path = generate_image(topic, output_path=image_output_path)
    
    # 5. Update the variable and print message
    print("\n🌄 Image saved to:\n", image_path)
    
    # --- END OF CHANGE ---

    print("\n💾 Exporting Final Content...")
    md_path = save_as_markdown(final_content, topic)
    pdf_path = save_as_pdf(final_content, topic)

    print(f"\n📄 Markdown saved to: {md_path}")
    print(f"📄 PDF saved to: {pdf_path}")

if __name__ == "__main__":
    main()