from staff import animal_items
from recall import go_market
from buy_horse import buy_horse
from ressurection import resurrect
from get_equipment_from_bank import search_items,equip_items

import time
import os

# Get the full path to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the json file
json_file_path = os.path.join(script_dir, 'equipped_items.json')

def dead():
    if Dead():
        time.sleep(10)
        resurrect()
        go_market()
        UseSkill("Hiding")
        for i in range(25):
                time.sleep(60)
                print(f"прошло {i+1} минут.")
        search_items(json_file_path)
        equip_items(json_file_path)
        buy_horse()
