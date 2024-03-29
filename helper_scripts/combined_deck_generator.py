from PIL import Image
import os
import sys

# Set the directory containing your JPEG images

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

if sys.argv[1] == 'Necro':
    classname, prefix = ['Necromancer','necro']
elif sys.argv[1] == 'Pyro':
    classname, prefix = ['Pyromancer','pyro']

image_directory = f'{parent_directory}/{classname}/{prefix}_cards_vector'

# Set the number of rows and columns for the grid
rows = 6
columns = 5

# Get a list of image file paths in the directory
image_files = [os.path.join(image_directory, filename) for filename in os.listdir(image_directory) if filename.endswith('.png')]

# Calculate the width and height of the individual images
image_width, image_height = Image.open(image_files[0]).size

# Create a new blank image with the dimensions of the grid
grid_width = columns * image_width
grid_height = rows * image_height
grid_image = Image.new('RGB', (grid_width, grid_height))

# Iterate through the image files and paste them into the grid
for i, image_file in enumerate(image_files):
    row = i // columns
    col = i % columns
    image = Image.open(image_file)
    grid_image.paste(image, (col * image_width, row * image_height))

# Save the final stacked image
grid_image.save(f'{parent_directory}/{prefix}_deck.jpg')

print('Stacked image saved as stacked_image.jpg')
