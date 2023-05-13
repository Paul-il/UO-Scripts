from staff import name,warrior_name,mage_name,scalp,loot,hunt_pack,zulucoin,skinning_Knife
from drink_tamla import tamla
from move_hides import hides
from dead import dead
from cheking_cast import check_cast
from befor_hunting import befor_hunt
from bow import take_bow

from tactic import (lesser_shadow_tactic, undead_tactic, mage_tactic,
                    warrior_tactic,great_wyrm
                    )

from datetime import datetime
from py_stealth import *

import time

def maintain_distance(min_distance):
    dead()
    for npc_type in name:
        if FindType(npc_type, Ground()):
            found_npc = GetFoundList()[0]
            npc_distance = GetDistance(found_npc)
            if npc_distance < min_distance:
                print(f"NPC {GetName(npc_type)} is too close. Moving away...")
                NewMoveXY(GetX(npc_type)-4, GetY(npc_type)-4, True, 1, True)
                NewMoveXY(GetX(npc_type)+4, GetY(npc_type)+4, True, 1, True)

def npcs_around(distance):
    dead()
    SetFindDistance(distance)
    for npc_type in name:
        if FindType(npc_type, Ground()):
            found_npc = GetFoundList()[0]
            npc_name = GetName(found_npc).lower()
            if "animal" in npc_name:
                print(f"Ignoring animal NPC: {npc_type}")
                Ignore(found_npc)
                continue
            if npc_type not in name:
                print(f"Ignoring unwanted NPC: {npc_type}")
                Ignore(found_npc)
                continue
            Ignore(npc_type)
            return True
    return False

def main_attack():
    print("Searching for npc...")
    while npcs_around(9):
        check_cast()
        dead()
        found = []
        for npc in name:
            if FindType(npc, Ground()):
                found += GetFindedList()
                Ignore(npc)
                dead()
                found = sorted(found, key=lambda x: (GetName(x).lower() != "a mage hunter", not any(word in GetName(x).lower() for word in ["mutant", "frankenstein", "dracula"])))
        maintain_distance(4)
        time.sleep(0.1)

        for npc in found:
            npc_name = GetName(npc)

            if npc_name == "a Great Wyrm":
                great_wyrm(npc, found)

            elif npc_name == "a Lesser Shadow":
                lesser_shadow_tactic(npc, found)

            elif "Undead" in npc_name or "Dracoliche" in npc_name:
                undead_tactic(npc, found)
                     
            elif any(mage in npc_name for mage in mage_name):
                mage_tactic(npc, found)
                
            elif any(warrior in npc_name for warrior in warrior_name):
                warrior_tactic(npc, found)
    print("No one is here.")                 
    main_loot()

def main_loot():
    found_corpse = []
    SetFindDistance(10)
    take_bow()
    dead()
    while True:
        dead()
        corpse = FindType(0x2006, Ground())
        found_corpse += GetFindedList()
        if not corpse:
            break

        NewMoveXY(GetX(corpse), GetY(corpse), True, 1, True)
        tamla()
        dead()
        if TargetPresent():
            CancelTarget()

        name = GetName(corpse)
        if str(name) in scalp or "Daemon" in str(name) or "Fiend" in str(name):
            start_time = datetime.now()
            UseType2(skinning_Knife)
            WaitTargetObject(corpse)
            time.sleep(1)
            if InJournalBetweenTimes("You are already doing something else.", start_time, datetime.now()) != -1:
                time.sleep(2)
                UseType2(skinning_Knife)
                WaitTargetObject(corpse)
                time.sleep(1)
                hides()
            dead()
            hides()
        print(f'Looting: {str(name)}')
        UseObject(corpse)
        if not GetMaxMana(Self()):
            SetWarMode(False)
            UseSkill("Meditation")

        for i in loot:
            dead()
            while FindTypeEx(i, 0xFFFF, corpse, False) > 0:
                item = FindItem()
                start_time = datetime.now()
                MoveItem(item, -1, hunt_pack, 0, 0, 0)
                time.sleep(0.1)
                if InJournalBetweenTimes("You are already holding the item", start_time, datetime.now()) != -1:
                    Disconnect()
                tamla()
                if FindType(zulucoin, Backpack()):
                    MoveItem(FindItem(), FindFullQuantity(), hunt_pack, 0, 0, 0)
                    time.sleep(0.5)

        Ignore(corpse)
        dead()
        main_attack()
    befor_hunt()


