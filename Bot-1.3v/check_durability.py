import re
from stealth import *

from recall import go_market, go_home
from change_class import crafter
from repair_bow import repair_bow

def check_weapon_durability():
    one_handed_weapon_id = ObjAtLayer(1)  # Right hand layer
    two_handed_weapon_id = ObjAtLayer(2)  # Left hand layer

    weapon_id = 0

    if one_handed_weapon_id:
        weapon_id = one_handed_weapon_id
    elif two_handed_weapon_id:
        weapon_id = two_handed_weapon_id

    if weapon_id == 0:
        print("No weapon equipped.")
        return

    weapon_tooltip = GetTooltip(weapon_id)
    weapon_name_match = re.search(r"(\d+ )?(.+?)\|", weapon_tooltip)

    if weapon_name_match:
        weapon_name = weapon_name_match.group(2)
    else:
        weapon_name = "Unknown"

    weapon_properties = weapon_tooltip.split("|")

    print(f"Weapon name: {weapon_name}")

    durability = None
    for prop in weapon_properties:
        if "durability" in prop.lower():
            durability = int(prop.split(" ")[1])

    if durability is not None and durability < 180:
        print(f"Weapon durability: {durability}")
        print("Need to fix my weapon.")
        go_market()
        crafter()
        go_home()
        repair_bow()
    else:
        print(f"Durability is normal: {durability}")
