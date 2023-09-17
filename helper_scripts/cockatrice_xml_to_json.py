import xml.etree.ElementTree as ET
from xmljson import badgerfish as bf
import json
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)

filename=parent_directory+'/Necromancer/necro_cockatrice_set'
# Parse the XML data
tree = ET.parse(f"{filename}.xml")  # Replace 'cards.xml' with the path to your XML file
root = tree.getroot()

# Convert XML to JSON using xmljson
json_data = bf.data(root)['cockatrice_carddatabase']['cards']

def remove_dollar_keys(data):
    if isinstance(data, dict):
        # Create a copy of the dictionary with '$' keys removed
        filtered_dict = {}
        for key, value in data.items():
            if key == "$":
                # Skip '$' key and just assign its value to filtered_dict
                filtered_dict = value
            else:
                # Recursively process other keys
                filtered_dict[key] = remove_dollar_keys(value)
        return filtered_dict
    elif isinstance(data, list):
        # Recursively process items in a list
        return [remove_dollar_keys(item) for item in data]
    else:
        return data

# Remove '$' keys
filtered_data = remove_dollar_keys(json_data)

# save the filtered data to a JSON file
with open(f"{filename}.json", 'w') as filtered_json_file:
    json.dump(filtered_data, filtered_json_file, indent=4)


