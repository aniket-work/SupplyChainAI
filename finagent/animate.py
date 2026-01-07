from PIL import Image
import imageio.v2 as imageio
import os
import numpy as np

def generate_title_animation(output_path="images/title-animation.gif"):
    """Creates an animated GIF by cycling through charts."""
    # Order: Performance -> Sentiment
    files = ["images/portfolio-performance.png", "images/sentiment-trends.png"]
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    images = []
    target_size = (1200, 800) # Standardize size
    
    for filename in files:
        if os.path.exists(filename):
            # Use PIL to resize for consistency
            img = Image.open(filename).convert('RGB')
            img = img.resize(target_size, Image.Resampling.LANCZOS)
            images.append(np.array(img))
        else:
            print(f"Warning: {filename} not found for animation.")

    if images:
        imageio.mimsave(output_path, images, duration=1000, loop=0) # duration in ms
        print(f"Generated animation: {output_path}")
    else:
        print("Error: No images found to create animation.")

if __name__ == "__main__":
    generate_title_animation()
