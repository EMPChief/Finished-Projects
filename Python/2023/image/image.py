from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance
import random


def enhance_image(image_path, output_folder):
    try:
        print(f"Processing image: {image_path}")
        play = Image.open(image_path)

        # Adjust contrast
        enhancer = ImageEnhance.Contrast(play)
        play = enhancer.enhance(1.2)

        # Adjust sharpness
        enhancer = ImageEnhance.Sharpness(play)
        play = enhancer.enhance(1.1)

        # Adjust brightness
        enhancer = ImageEnhance.Brightness(play)
        play = enhancer.enhance(1.1)

        # Adjust color
        enhancer = ImageEnhance.Color(play)
        play = enhancer.enhance(1.1)

        # Apply a milder smoothing filter (BLUR for a subtle effect)
        play = play.filter(ImageFilter.BLUR)

        # Save the enhanced image
        ran = random.randint(0, 1000000000000)
        output_path = output_folder / f'enhanced_img{ran}.png'
        print(f"Saving the enhanced image to {output_path}...")
        play.save(output_path)

    except Exception as e:
        print(f"Error processing {image_path}: {e}")


if __name__ == "__main__":
    # Specify input and output folders using pathlib.Path (relative paths)
    input_folder = Path('input_folder')
    output_folder = Path('edited')

    # Resolve to absolute paths
    input_folder = Path(__file__).resolve().parent / input_folder
    output_folder = Path(__file__).resolve().parent / output_folder

    # Create the output folder if it doesn't exist
    output_folder.mkdir(parents=True, exist_ok=True)

    # Process each image in the input folder
    for image_path in input_folder.glob('*.*'):
        if image_path.is_file() and image_path.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif'}:
            enhance_image(image_path, output_folder)

    print("All images processed.")
