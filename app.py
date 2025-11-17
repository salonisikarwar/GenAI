import os
from flask import Flask, render_template, request, url_for
from agents.langgraph_pipeline import graph
from agents.langchain_pipeline import chain
from agents.image_agent import generate_image
from utils.exporter import save_as_markdown, save_as_pdf

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form.get("topic")
        content_type = request.form.get("content_type")
        tone = request.form.get("tone")
        pipeline = request.form.get("pipeline")

        combined_topic = f"{topic} ({content_type})"

        if pipeline == "chain":
            result = chain.invoke({
                "topic": combined_topic,
                "tone": tone
            })
        else:
            result = graph.invoke({
                "topic": combined_topic,
                "tone": tone
            })

        final_content = result["final"]
        seo_keywords = result["keywords"]

        # --- THIS IS THE CORRECTED IMAGE LOGIC ---
        
        # 1. Create a safe, unique filename for the image
        safe_topic_name = topic.replace(' ', '_').lower().replace('(', '').replace(')', '')
        image_filename = f"{safe_topic_name}_image.png"
        
        # 2. Define the full path to save the image (inside the 'static' folder)
        image_save_path = os.path.join("static", image_filename)
        
        # 3. Call the agent and pass the new, unique output_path
        image_result_path = generate_image(combined_topic, output_path=image_save_path)
        
        # 4. Create the URL for the template
        image_url_for_template = None
        if not image_result_path.startswith("[Error]"):
            # Use the filename we already know
            image_url_for_template = url_for("static", filename=image_filename) 
        else:
            # Log the error to your terminal
            print(f"IMAGE GENERATION FAILED: {image_result_path}")
            
        # --- END OF CORRECTION ---

        md_filename = save_as_markdown(final_content, topic)
        pdf_filename = save_as_pdf(final_content, topic)

        md_link = url_for("static", filename=f"exports/{md_filename}")
        pdf_link = url_for("static", filename=f"exports/{pdf_filename}")

        return render_template(
            "index.html",
            topic=topic,
            content_type=content_type,
            tone=tone,
            pipeline=pipeline,
            content=final_content,
            seo_keywords=seo_keywords,
            image_url=image_url_for_template,  # Pass the correct, unique URL
            md_link=md_link,
            pdf_link=pdf_link
        )

    return render_template("index.html", topic=None)

if __name__ == "__main__":
    app.run(debug=True)