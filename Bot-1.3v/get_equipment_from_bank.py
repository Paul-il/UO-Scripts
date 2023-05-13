from staff import animal_items,sumka

from py_stealth import *
import time
import re
import os
import json

def search_items(json_file_path):
    print("search_items")
    UOSay("bank")
    time.sleep(0.5)
    try:
        if FindTypeEx(sumka,0xFFFF,ObjAtLayer(BankLayer()),True):
            _foundList = GetFindedList()
            for _found in _foundList:
                UseObject(_found)
                with open(json_file_path, 'r') as f:
                    equipped_items = json.load(f)
                for item_serial, item_info in equipped_items.items():
                    time.sleep(0.5)
                    if FindTypeEx(item_info['type'], item_info['color'], _found, True):
                        MoveItem(FindItem(), -1, Backpack(), 0, 0, 0)
                        time.sleep(0.5)

        for item in animal_items:
            MoveItem(item, -1, Backpack(), 0, 0, 0)
            time.sleep(0.5)
    except Exception as e:
        print(f"ERROR: {e}")


def equip_items(json_file_path):
    with open(json_file_path, 'r') as f:
        equipped_items = json.load(f)
        
    backpack_contents = GetItemsInContainer(Backpack())
    backpack_serials = [item['serial'] for item in backpack_contents]
    for item_serial_str, item_info in equipped_items.items():
        layer = item_info['layer']
        if not ObjAtLayer(layer):
            item_serial_int = int(item_serial_str, 16)
            if item_serial_int in backpack_serials:
                item_info_backpack = next((item for item in backpack_contents if item['serial'] == item_serial_int), None)
                if item_info_backpack:
                    print(f"Found item in backpack: {item_info_backpack['name']}")
                    UseObject(item_serial_int)
                    print(f"Clicking on item: {item_info_backpack['name']}")
                    time.sleep(0.5)
                else:
                    print(f"Cannot equip {item_info_backpack['name']}, it is not in the backpack")

def GetItemsInContainer(container_id):
    FindType(-1, container_id)
    found_items_serials = GetFoundList()
    items_info = []
    for serial in found_items_serials:
        item_tooltip = GetTooltip(serial)
        item_name_match = re.search(r"(\d+ )?(.+?)\|", item_tooltip)
        if item_name_match:
            item_name = item_name_match.group(2)
        else:
            item_name = "Unknown"
        item_info = {
            "serial": serial,
            "name": item_name,
            "type": GetType(serial),
            "color": GetColor(serial)
        }
        items_info.append(item_info)
    return items_info

"""# Get the full path to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the json file
json_file_path = os.path.join(script_dir, 'equipped_items.json')

search_items(json_file_path)"""