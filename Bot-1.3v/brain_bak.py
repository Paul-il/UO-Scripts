from staff import name,warrior_name,mage_name,scalp,loot,hunt_pack,zulucoin,skinning_Knife
from drink_tamla import tamla
from move_hides import hides
from dead import dead
from cheking_cast import check_cast
from befor_hunting import befor_hunt
#from check_durability import check_weapon_durability
from bow import take_bow

from datetime import datetime
from py_stealth import *

import time

def movement(npc):
    SetWarMode(True)
    Attack(npc)
    NewMoveXY(GetX(npc)+1, GetY(npc)-1, True, 1, True)
    time.sleep(3)
    NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
    time.sleep(3)
    NewMoveXY(GetX(npc)+2, GetY(npc)+2, True, 1, True)
    tamla()
    dead()

def maintain_distance(min_distance):
    dead()
    for npc_type in name:
        if FindType(npc_type, Ground()):
            found_npc = GetFoundList()[0]
            npc_distance = GetDistance(found_npc)
            if npc_distance < min_distance:
                print(f"NPC {npc_type} is too close. Moving away...")
                NewMoveXY(GetX(npc_type)-4, GetY(npc_type)-4, True, 1, True)

def npcs_around(distance):
    dead()
    print(f"Checking NPCs around with distance: {distance}")
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
            print(f"Found NPC: {npc_type}")
            Ignore(npc_type)
            return True
    print("No NPCs found")
    return False

def main_attack():
    print("main_attack")
    while npcs_around(9):
        check_cast()
        dead()
        print("Inside the npcs_around_while loop")
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

            if npc_name == "a Lesser Shadow":
                # код для "a Lesser Shadow"
                print("a Lesser Shadow")
                Disarm()
                SetWarMode(False)
                NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
                while GetHP(npc) > 0:
                    print(f"Index: {found.index(npc)}, Name: {str(GetName(npc))}, Distance: {GetDistance(npc)}")
                    NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
                    start_time = datetime.now()
                    CastToObject("chain lightning", npc)
                    time.sleep(2)
                    dead()
                    if InJournalBetweenTimes("I can't see that.", start_time, datetime.now()) != -1:
                        movement(npc)
                    while Paralyzed():
                        print("Paralyzed")
                        NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
                        NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
                        tamla()

            elif "Undead" in npc_name or "Dracoliche" in npc_name:
                # код для "Undead" или "Dracoliche"
                take_bow()
                SetWarMode(True)
                while GetHP(npc) > 0:
                    take_bow()
                    Attack(npc)
                    CastToObject("resurrection", npc)
                    NewMoveXY(GetX(npc)-4, GetY(npc)+4, True, 1, True)
                    tamla()
                    dead()
                    while Paralyzed():
                        print("Paralyzed")
                        NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
                        NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
                        tamla()
                        
            elif any(mage in npc_name for mage in mage_name):
                # код для магов из списка mage_name
                take_bow()
                SetWarMode(True)
                NewMoveXY(GetX(npc)-4, GetY(npc)-4, True, 1, True)
                while GetHP(npc) > 0:
                    print(f"Index: {found.index(npc)}, Name: {GetName(npc)}, Distance: {GetDistance(npc)}")
                    Attack(npc)
                    dead()
                    if GetMana(Self()) > 50:
                        start_time = datetime.now()
                        CastToObject("chain lightning", npc)
                        print("lightning")
                        Wait(2000)
                        dead()
                    else:
                        movement(npc)
                    if InJournalBetweenTimes("I can't see that", start_time, datetime.now()) != -1:
                        print("Moving to another place")
                        movement(npc)
                    while Paralyzed():
                        print("Paralyzed")
                        NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
                        NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
                        tamla()

            elif any(warrior in npc_name for warrior in warrior_name):
                # код для воинов из списка warrior_name
                movement(npc)
                while GetHP(npc) > 0:
                    dead()
                    print(f"Number: {found.index(npc)}, Name: {str(GetName(npc))}, Distance: {GetDistance(npc)}")
                    movement(npc)
                    while Paralyzed():
                        print("Paralyzed")
                        NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
                        NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
                        tamla()
                        NewMoveXY(GetX(npc), GetY(npc), True, 1, True)

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


