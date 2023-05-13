from staff import sunduk,hunt_pack,arrows,fish,bottle,tamla_color,bandages,sumka

from py_stealth import *

def unload():
    MoveXYZ(2849,173,26,True,1,True)
    UseObject(sunduk)
    if FindType(sumka, Backpack()):
        EmptyContainer(hunt_pack,sunduk,50)
    else:
        print("No HuntPack in Backpack")
    
def move_items_if_needed(item, color, target_quantity, source_container, target_container):
    if isinstance(item, tuple):
        item, color = item
    else:
        color = 0x0000
    FindTypeEx(item, color, Backpack(), False)
    if FindFullQuantity() < target_quantity:
        print(f"Amount of {GetName(item)} in Backpack: {FindFullQuantity()}.")
        result = target_quantity - FindFullQuantity()
        FindTypeEx(item, color, source_container, False)
        MoveItem(FindItem(), result, target_container, 0, 0, 0)
        Wait(500)

def load():
    MoveXYZ(2849, 173, 26, True, 1, True)
    UseObject(sunduk)

    items_to_check = {
    arrows: (0x0000, 1000, sunduk, hunt_pack),
    bandages: (0x0000, 1000, sunduk, hunt_pack),
    BP(): (0x0000, 100, sunduk, hunt_pack),
    BM(): (0x0000, 100, sunduk, hunt_pack),
    GA(): (0x0000, 100, sunduk, hunt_pack),
    GS(): (0x0000, 100, sunduk, hunt_pack),
    MR(): (0x0000, 100, sunduk, hunt_pack),
    NS(): (0x0000, 100, sunduk, hunt_pack),
    SA(): (0x0000, 100, sunduk, hunt_pack),
    SS(): (0x0000, 100, sunduk, hunt_pack),
    fish: (0x0000, 20, sunduk, Backpack()),
    bottle: (tamla_color, 10, sunduk, hunt_pack)
    }

    for item, (color, target_quantity, source_container, target_container) in items_to_check.items():
        move_items_if_needed(item, color, target_quantity, source_container, target_container)
