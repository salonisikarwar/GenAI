import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from io import BytesIO
from PIL import Image

load_dotenv()

client = InferenceClient(token=os.getenv("HF_TOKEN"))

def generate_image(topic: str, output_path: str = "static/generated_image.png") -> str:
    """
    Generates an image from a topic and saves it to a file.
    Returns the file path.
    """
    prompt = f"A high-quality, professional, AI-generated illustration for: {topic}"

    try:
        # This call now returns a PIL Image object directly, not bytes
        image = client.text_to_image(
            prompt,
            model="stabilityai/stable-diffusion-xl-base-1.0"
        )
        
        # --- THIS LINE WAS THE ERROR AND IS NOW REMOVED ---
        # image = Image.open(BytesIO(image_bytes)) 
        # --- (We already have an 'image' object) ---
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save the PIL Image object directly
        image.save(output_path)
        
        return output_path

    except Exception as e:
        return f"[Error] {str(e)}"

if __name__ == '__main__':
    # A test to see if it works
    print("Generating image...")
    result_path = generate_image("a photorealistic cat wearing a tiny astronaut helmet", "static/test_image.png")
    print(f"Result: {result_path}")