import os
from PIL import Image
from typing import List


# palette.png generate with below command
# convert -size 1x3 xc:black xc:white xc:red +append palette.png
# fmt: off
PALETTE_BWR = [
    0, 0, 0,  # black
    255, 255, 255,  # white
    255, 0, 0,  # red
]

PALETTE_BW = [
    0, 0, 0,  # black
    255, 255, 255,  # white
]

PALETTE_BWY = [
    0, 0, 0,  # black
    255, 255, 255,  # white
    255, 255, 0,  # yellow
]

PALETTE_BWRY = [
    0, 0, 0,  # black
    255, 255, 255,  # white
    255, 0, 0,  # red
    255, 255, 0,  # yellow
]
# fmt: on


# remap the image to the given palette
# convert input.jpg -dither FloydSteinberg -define dither:diffusion-amount=85% -remap palette.png bmp:output.bmp
def remap_image(
    input_path: str,
    output_path: str,
    palette: List[int],
    dither=Image.Dither.FLOYDSTEINBERG,
    color_tolerance: int = 30,
) -> str:
    with Image.open(input_path) as original_image:
        original_image = original_image.convert("RGB")
        
        # Pre-process similar colors
        width, height = original_image.size
        pixels = original_image.load()
        
        # Convert palette list to RGB tuples for easier comparison
        palette_colors = [(palette[i], palette[i+1], palette[i+2]) 
                         for i in range(0, len(palette), 3)]
        
        # Create a new image for pre-processed colors
        processed_image = Image.new("RGB", original_image.size)
        processed_pixels = processed_image.load()
        
        # Process each pixel
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                
                # Find the closest palette color
                min_distance = float('inf')
                closest_color = None
                
                for palette_color in palette_colors:
                    # Calculate color distance (using simple RGB distance)
                    distance = sum((a - b) ** 2 for a, b in zip(pixel, palette_color))
                    
                    if distance < min_distance:
                        min_distance = distance
                        closest_color = palette_color
                
                # If the color is within tolerance, use the palette color directly
                if min_distance <= color_tolerance ** 2:
                    processed_pixels[x, y] = closest_color
                else:
                    processed_pixels[x, y] = pixel

        # Create a new image using the 'P' mode (palette-based)
        palette_image = Image.new("P", original_image.size)
        palette_image.putpalette(palette)

        # Convert the processed image to 'P' mode with our custom palette
        converted_image = processed_image.quantize(
            palette=palette_image, 
            dither=dither
        )

        # Convert back to RGB mode before saving as JPEG
        converted_image = converted_image.convert('RGB')

        # Save the image
        converted_image.save(output_path, 'JPEG', quality="maximum")

    return output_path


if __name__ == "__main__":
    pass