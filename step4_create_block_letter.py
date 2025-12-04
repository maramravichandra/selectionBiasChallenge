
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_block_letter_s(height: int, width: int, letter: str = "S", font_size_ratio: float = 0.9) -> np.ndarray:
    """
    Generates a block letter 'S' matching image dimensions.

    Args:
        height: The height of the output image.
        width: The width of the output image.
        letter: The letter to generate.
        font_size_ratio: The ratio of the font size to the image height.

    Returns:
        A 2D numpy array (height × width) with values in [0, 1]
        where the letter is black (0.0) on a white background (1.0).
    """
    # Create a new image with a white background
    img = Image.new('L', (width, height), color=255)
    draw = ImageDraw.Draw(img)

    # Find a suitable font
    font_path = None
    font_paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "arial.ttf"
    ]
    for path in font_paths:
        try:
            font = ImageFont.truetype(path, size=int(height * font_size_ratio))
            font_path = path
            break
        except IOError:
            continue

    if font_path is None:
        # If no font is found, use a default font
        font = ImageFont.load_default()

    # Calculate text size and position
    try:
        # Modern Pillow versions
        bbox = draw.textbbox((0, 0), letter, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except AttributeError:
        # Older Pillow versions
        text_width, text_height = draw.textsize(letter, font=font)


    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Draw the letter on the image
    draw.text((x, y), letter, font=font, fill=0)

    # Convert to numpy array and normalize
    np_img = np.array(img) / 255.0

    return np_img
