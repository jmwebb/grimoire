from PIL import Image, ImageDraw, ImageFont
import json
import textwrap

# Load card data from JSON
with open('necro_cockatrice_set.json', 'r') as json_file:
    card_data = json.load(json_file)
    print(card_data)

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
    image_height = card_height//2  # Full card height
    image_position = (2*border_width, 2*border_width)  # Top-left corner of the card image

    # Add card name and text
    font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 12)  # Adjust the font and size as needed
    name_font = ImageFont.truetype("/Library/Fonts//Arial Unicode.ttf", 16) 
    text_color = (0, 0, 0)

 
    name_pos= (10, card_height-card_height/2+10)
    text_pos= (10, card_height-card_height/2+50)
    # Wrap the text to fit within the available space
    text = "\n".join(textwrap.wrap(data['text'], width=30))  # Adjust the width as needed
    name="\n".join(textwrap.wrap(data['name'], width=30)) 

    draw.text(name_pos, name, fill=text_color, font=name_font)
    draw.text(text_pos, text, fill=text_color, font=font)

    # Load and paste the card image (replace 'image_path' with the actual image path)
    card_image_data = Image.open(f"necro_art/{data['name']}.jpg")
    card_image_data = card_image_data.resize((image_width, image_height))
    
    card_image.paste(card_image_data, image_position)

    return card_image

# Generate card images and save them
for card in card_data['card']:
    card_image = create_card_image(card)
    card_image.save(f"necro_cards/{card['name']}.png")

# card_image = create_card_image(card_data['card'][0])
# card_image.save(f"card_images/{card_data['card'][0]['name']}7.png")
# Optionally, you can display or further process the generated card images
