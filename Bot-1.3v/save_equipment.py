import os
import re
import json
from py_stealth import *

# Get the full path to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the json file
json_file_path = os.path.join(script_dir, 'equipped_items.json')

def save_equipment(json_file_path):
    layers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 26, 27]
    equipped_items = {}
    
    for layer in layers:
        item_id = ObjAtLayer(layer)
        if item_id:
            name = GetTooltip(item_id)
            item_name_match = re.search(r"(\d+ )?(.+?)\|", name)
            if item_name_match:
                item_name = item_name_match.group(2)
            else:
                item_name = "Unknown"
            item_info = {
                "serial": hex(item_id),
                "name": item_name,
                "type": GetType(item_id),
                "color": GetColor(item_id),
                "layer": layer
            }
            equipped_items[hex(item_id)] = item_info

    with open(json_file_path, 'w') as f:
        json.dump(equipped_items, f)
