# Day 18 - save module to save screen contents to a .png file.

# Import the Image class from PIL module.
from PIL import Image

# Import os module to remove .eps file.
import os

# Define function to save screen image to .png file.
def save_image(screen, filename):

    # Get the screen canvas
    canvas = screen.getcanvas()

    # Grab screen image and save to .eps file.
    canvas.postscript(file="../image-files/" + filename + ".eps")

    # Fetch screen image from saved .eps file.
    image = Image.open("../image-files/" + filename + ".eps")

    # Save screen image as .png file.
    image.save("../image-files/" + filename + ".png")

    # Remove .eps image file.
    os.remove("../image-files/" + filename + ".eps")



