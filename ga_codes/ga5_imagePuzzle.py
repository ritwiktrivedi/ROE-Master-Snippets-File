from PIL import Image
import numpy as np

# Load the scrambled image
scrambled_img = Image.open(".\jigsaw.webp")
# path has been adjusted for windows.... adjust for colab if you use it there.

# Define grid size
GRID_SIZE = 5
PIECE_SIZE = scrambled_img.width // GRID_SIZE  # 100 pixels per piece

# Define the mapping of scrambled positions to original positions
mapping = [
    (2, 1, 0, 0), (1, 1, 0, 1), (4, 1, 0, 2), (0, 3, 0, 3), (0, 1, 0, 4),
    (1, 4, 1, 0), (2, 0, 1, 1), (2, 4, 1, 2), (4, 2, 1, 3), (2, 2, 1, 4),
    (0, 0, 2, 0), (3, 2, 2, 1), (4, 3, 2, 2), (3, 0, 2, 3), (3, 4, 2, 4),
    (1, 0, 3, 0), (2, 3, 3, 1), (3, 3, 3, 2), (4, 4, 3, 3), (0, 2, 3, 4),
    (3, 1, 4, 0), (1, 2, 4, 1), (1, 3, 4, 2), (0, 4, 4, 3), (4, 0, 4, 4)
]

# Create a blank image for the reconstructed result
reconstructed_img = Image.new(
    "RGB", (scrambled_img.width, scrambled_img.height))

# Reassemble the image based on the mapping
for original_row, original_col, scrambled_row, scrambled_col in mapping:
    # Extract the scrambled piece
    scrambled_x = scrambled_col * PIECE_SIZE
    scrambled_y = scrambled_row * PIECE_SIZE
    piece = scrambled_img.crop(
        (scrambled_x, scrambled_y, scrambled_x + PIECE_SIZE, scrambled_y + PIECE_SIZE))

    # Place it in the original position
    original_x = original_col * PIECE_SIZE
    original_y = original_row * PIECE_SIZE
    reconstructed_img.paste(piece, (original_x, original_y))

# Save the reconstructed image
reconstructed_img.save("reconstructed_image.png")
print("Reconstructed image saved as reconstructed_image.png")
