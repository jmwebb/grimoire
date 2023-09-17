from PIL import Image, ImageDraw, ImageFont
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

# Create a function to generate card images
def create_card_image(data):
    card_width = 200  # Adjust as needed
    card_height = 300  # Adjust as needed

    # Create a blank card image
    card_image = Image.new('RGB', (card_width, card_height), (255, 255, 255))
    draw = ImageDraw.Draw(card_image)

    # Draw card borders and decorations
    border_color = (0, 0, 0)
    border_width = 5
    draw.rectangle([(border_width, border_width), (card_width - border_width, card_height - border_width)],
                   outline=border_color, width=border_width)

    # Calculate dimensions for the card image
    image_width = card_width-4*border_width   # Half of the card width
    image_height = int(card_height//2.3)  # Full card height
    image_position = (2*border_width, 2*border_width+30)  # Top-left corner of the card image

    # Define Fonts
    name_font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 18) 
    manacost_font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 14) 
    text_color = (0, 0, 0)

 
    name_pos= (20, 10)
    text_pos= (20, card_height-card_height/2+20)
  
    #add card name
    name="\n".join(textwrap.wrap(data['name'], width=30)) #wrap text so it doesn't run off card
    draw.text(name_pos, name, fill=text_color, font=name_font)

    #add card text
    if data['text']:
        wrapped_lines= textwrap.wrap(data['text'], width=30)

        if len(wrapped_lines)>5:
            font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 10)  # Adjust the font and size as needed
        else:
            font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 12)  # Adjust the font and size as needed

        text = "\n".join(wrapped_lines)  # Adjust the width as needed
        draw.text(text_pos, text, fill=text_color, font=font)

    #add mana cost
    if 'manacost' in data['prop'].keys():
        text = "\n".join(textwrap.wrap(f"Mana: {data['prop']['manacost']}", width=30))  # Adjust the width as needed
        draw.text((20, card_height-6*border_width), text, fill=(0,0,255), font=manacost_font)

    #add power/health
    if 'pt' in data['prop'].keys():
        text = "\n".join(textwrap.wrap(f"Atk/HP: {data['prop']['pt']}", width=30))  # Adjust the width as needed
        draw.text((card_width-90, card_height-6*border_width), text, fill=(0,0,255), font=manacost_font)
        



    # Load and paste the card image (replace 'image_path' with the actual image path)
    card_image_data = Image.open(f"{parent_directory}/{classname}/{prefix}_art/{data['name']}.jpg")
    card_image_data = card_image_data.resize((image_width, image_height))
    
    card_image.paste(card_image_data, image_position)

    return card_image

# Generate card images and save them
for card in card_data['card']:
    card_image = create_card_image(card)
    card_image.save(f"{parent_directory}/{classname}/{prefix}_cards/{card['name']}.png")

# card_image = create_card_image(card_data['card'][0])
# card_image.save(f"card_images/{card_data['card'][0]['name']}7.png")
# Optionally, you can display or further process the generated card images
