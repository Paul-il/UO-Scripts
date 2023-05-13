from recall import teleport
from hunt_location import hunt
from runebook import charge_runebook
from load_unload import unload,load
from save_equipment import save_equipment
from check_durability import check_weapon_durability
from bow import take_bow
from dead import dead
from staff import home

import os
from datetime import datetime
from py_stealth import *

# Get the full path to the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the json file
json_file_path = os.path.join(script_dir, 'equipped_items.json')

def main():
    SetMoveOpenDoor(True)
    SetMoveCheckStamina(True)
    dead()
    take_bow()
    save_equipment(json_file_path)
    print("equipment saved")
    check_weapon_durability()
    hunt()
    teleport(home,2846,173)
    unload()
    load()
    charge_runebook()
    ClearSystemJournal()



if __name__ == "__main__":
    timea = datetime.now()
    while True:
        main()
