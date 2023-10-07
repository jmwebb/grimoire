
import xml.dom.minidom as minidom
import cairosvg
import json
import os
import sys
import base64

convert_to_pngs=False

if sys.argv[1] == 'Necro':
    classname, prefix = ['Necromancer','necro']
elif sys.argv[1] == 'Pyro':
    classname, prefix = ['Pyromancer','pyro']
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

# Load card data from JSON
with open(f'{parent_directory}/{classname}/{prefix}_cockatrice_set.json', 'r') as json_file:
    card_data = json.load(json_file)

# Load the SVG template
with open(f'{parent_directory}/card_design/{prefix}_template.svg', "r") as file:
    svg_data = file.read()

# Find the element by its ID
name_id = "text1089"
text_id = "text839"
mana_id = "text990-1"#tspan988-8
attack_id = "text990-5"#tspan988-3
HP_id = "text990"#tspan988

for card in card_data['card']:
    # Load the template SVG using minidon
    dom = minidom.parseString(svg_data)

    card_name=card['name']
    card_text=card['text']
    manacost=None
    power_toughness=None
    if 'manacost' in card.keys():
        manacost=card['manacost']
    if 'pt' in card.keys():
        power_toughness=card['pt']

    elements = dom.getElementsByTagName("tspan")  # Change "text" to the appropriate tag name
    for element in elements:
        for node in [node for node in element.childNodes if node.nodeValue is not None]:

            template_text= node.nodeValue.strip()

            if template_text == 'Card Name':
                node.nodeValue = card_name

            if template_text == 'Card Text':
                node.nodeValue = card_text

            if template_text == 'M' and manacost:
                node.nodeValue = manacost

            if template_text == 'P' and power_toughness:
                node.nodeValue =power_toughness.strip('/')[0]

            if template_text == 'T' and power_toughness:
                node.nodeValue =power_toughness.strip('/')[1]


    # Encode the new image data in base64
    with open(f"{parent_directory}/{classname}/{prefix}_art/{card_name}.jpg", "rb") as image_file:
        new_image_data = image_file.read()
    new_base64_data = base64.b64encode(new_image_data).decode("utf-8")

    # Find the <image> element by its ID
    image_id = "image2515"  
    elements = dom.getElementsByTagName("image")  
    for element in elements:
        if element.getAttribute('id')==image_id:
            # Replace the xlink:href attribute with the new image data
            new_xlink_href = f"data:image/jpeg;base64,{new_base64_data}"
            element.setAttribute("xlink:href", new_xlink_href)

    # Save the modified SVG to a new file
    output_svg_filename=f"{parent_directory}/{classname}/{prefix}_cards_vector/{card_name}.svg"
    output_png_filename=f"{parent_directory}/{classname}/{prefix}_cards/{card_name}.png"
    
    with open(output_svg_filename, "w") as file:
        file.write(dom.toxml())

    if convert_to_pngs:
        output_png_filename=output_png_filename.replace(" ",r"\ ")
        output_svg_filename=output_svg_filename.replace(" ",r"\ ")
        os.system(f'/Applications/Inkscape.app/Contents/MacOS/inkscape --export-type png --export-filename {output_png_filename} -w 1024 {output_svg_filename}')



