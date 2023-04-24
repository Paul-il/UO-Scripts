from staff import name

mage_hunter = "a Mage Hunter"
lesser_shadow = "a Lesser Shadow"

mage_dis = 8
warrior_dis = 4

def main_attack():
    found = []
    dis_found = []
    SetFindDistance(8)
    for npc in name:
        if FindType(npc, Ground()):
            found += GetFindedList()
            Ignore(npc)
    return found

print(main_attack(found))