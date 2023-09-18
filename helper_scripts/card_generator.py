from PIL import Image, ImageDraw, ImageFont
from svglib.svglib import svg2rlg
from reportlab.graphics.renderPM import drawToPIL, Drawing
import json
import textwrap
import os
import sys

if sys.argv[1] == 'Necro':
    classname, prefix = ['Necromancer','necro']
elif sys.argv[1] == 'Pyro':
    classname, prefix = ['Pyromancer','pyro']
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

# Load card data from JSON
with open(f'{parent_directory}/{classname}/{prefix}_cockatrice_set.json', 'r') as json_file:
    card_data = json.load(json_file)

#Load vector images for card symbols
# Load the SVG images using the 'svglib.svg2rlg()' function
icon1 = svg2rlg('mana_symbol.svg')

x1, y1, x2, y2 = icon1.getBounds()
# Set the size of the icons
image_scale=4

xscale, yscale = (0.5*image_scale, 0.5*image_scale)
icon1.scale(xscale,yscale)
icon1.width=(3+x2-x1)*xscale
icon1.height=(3+y2-y1)*yscale

# Create a function to generate card images
def create_card_image(data, image_scale):

    card_width = 200*image_scale  # Adjust as needed
    card_height = 300*image_scale # Adjust as needed

    # Create a blank card image
    card_image = Image.new('RGBA', (card_width, card_height), (256, 256, 256, 256))
    draw = ImageDraw.Draw(card_image)

    # Draw card borders and decorations
    border_color = (0, 0, 0)
    border_width = 5*image_scale
    draw.rounded_rectangle([(0, 0), (card_width, card_height)],
                   outline=border_color, width=border_width, radius=10*image_scale)

    # Calculate dimensions for the card image
    image_width = card_width-4*border_width   
    image_height = int(card_height//2.3)  
    image_position = (2*border_width, 2*border_width+30*image_scale)  # Top-left corner of the card image

    #Draw image border
    draw.rounded_rectangle([image_position, (image_width+2*border_width, image_height+2*border_width)],radius=10*image_scale)
    # Define Fonts
    name_font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 18*image_scale) 
    manacost_font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 22*image_scale) 
    pt_font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 14*image_scale) 
    text_color = (0, 0, 0)

 
    name_pos= (20*image_scale, 10*image_scale)
    text_pos= (20*image_scale, card_height-card_height/2+20*image_scale)
  
    icon = drawToPIL(icon1)
    card_image.paste(icon, (card_width-40*image_scale, 6*image_scale))

    #add card name
    name="\n".join(textwrap.wrap(data['name'], width=30)) #wrap text so it doesn't run off card
    draw.text(name_pos, name, fill=text_color, font=name_font)

    #add card text
    if data['text']:
        wrapped_lines= textwrap.wrap(data['text'], width=30)

        if len(wrapped_lines)>5:
            font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 10*image_scale)  # Adjust the font and size as needed
        else:
            font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 12*image_scale)  # Adjust the font and size as needed

        text = "\n".join(wrapped_lines)  # Adjust the width as needed
        draw.text(text_pos, text, fill=text_color, font=font)

    #add mana cost
    if 'manacost' in data['prop'].keys():
        text = "\n".join(textwrap.wrap(f"{data['prop']['manacost']}", width=30))  # Adjust the width as needed
        draw.text((card_width-30*image_scale, 7*image_scale), text, fill=(0,0,255), font=manacost_font)

    #add power/health
    if 'pt' in data['prop'].keys():
        text = "\n".join(textwrap.wrap(f"Atk/HP: {data['prop']['pt']}", width=30))  # Adjust the width as needed
        draw.text((card_width-90*image_scale, card_height-6*border_width), text, fill=(0,0,255), font=pt_font)


    # Load and paste the card image (replace 'image_path' with the actual image path)
    if os.path.isfile(f"{parent_directory}/{classname}/{prefix}_art/{data['name']}.jpg"):
        card_image_data = Image.open(f"{parent_directory}/{classname}/{prefix}_art/{data['name']}.jpg")
        card_image_data = card_image_data.resize((image_width, image_height))
        card_image.paste(card_image_data, image_position)


    return card_image

# Generate card images and save them
for card in card_data['card']:
    card_image = create_card_image(card, image_scale)
    card_image.save(f"{parent_directory}/{classname}/{prefix}_cards/{card['name']}.png")

# card_image = create_card_image(card_data['card'][0])
# card_image.save(f"card_images/{card_data['card'][0]['name']}7.png")
# Optionally, you can display or further process the generated card images
