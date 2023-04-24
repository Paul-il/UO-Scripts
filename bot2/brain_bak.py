from staff import name,msg_crafter,msg_hunter,warrior_name,mage_name,scalp,loot,hunt_pack,zulucoin,hide,skinning_Knife,undead_mage,mageHunter
from staff import shadow
from cast_healing import tamla
from cheking import dead,befor_hunt,zulucoin,medit,hides
from dress import take_kryss,take_bow
from datetime import datetime
from py_stealth import *

import time
import math

def main_attack():
    found = []
    dis_found = []
    SetFindDistance(10)
    for npc in name:
        if FindType(npc, Ground()):
            found += GetFindedList()
            Ignore(npc)
    for npc in found:
        if str(GetName(npc)) is "a Mage Hunter":
            print("Mage Hunter")
            AttackNPC(npc)
        elif str(GetName(npc)) is "shadow":
            print("a Shadow")
            Disarm()
            SetWarMode(False)
            CastToObj("chain lightning", npc)
            Wait(2000)
            NewMoveXY(GetX(npc) + 8, GetY(npc) - 8, True, 1, True)
        elif str(GetName(npc)) is "undead":
            CastToObj("resurrection", npc)
            AttackNPC(npc)
        elif any(npc is mage for mage in mage_name):
            AttackNPC(npc)
        elif any(npc is warrior for warrior in warrior_name):
            AttackNPCWarrior(npc)


    while Paralyzed():
        print("Paralyzed")
        NewMoveXY(GetX(npc) + 4, GetY(npc) - 4, True, 1, True)
        tamla()
        dead()

    while True:
        dis_found = [get_npc_distance(npc) for npc in found]
        dis_found = [x for x in dis_found if x is not None]
        if len(dis_found) == 0:
            break
        print(dis_found)
        time.sleep(1)


def get_npc_distance(npc):
    if npc not in found:
        return None
    player_location = (GetX(Self()), GetY(Self()))
    npc_location = (GetX(npc), GetY(npc))
    if None in player_location or None in npc_location:
        return None
    distance = math.sqrt((npc_location[0] - player_location[0])**2 + (npc_location[1] - player_location[1])**2)
    if GetHP(npc) <= 0:
        Ignore(npc)
    return (npc, distance)



def AttackNPCWarrior(npc):
    if WarMode() != True:
        SetWarMode(True)
    take_kryss()
    while GetHP(npc) > 0:
        Attack(npc)
        NewMoveXY(GetX(npc), GetY(npc), True, 1, True)
        tamla()

def AttackNPC(npc):
    if WarMode() != True:
        SetWarMode(True)
    take_bow()
    while GetHP(npc) > 0:
        if GetMana(Self()) > 50:
            CastToObj("chain lightning", npc)
            Wait(2000)
        else:
            NewMoveXY(GetX(npc) + 20, GetY(npc) - 20, True, 1, True)
            main_attack()
            medit()

    dead()
    main_loot()

def main_loot():
    found_corpse = []
    SetFindDistance(10)
    take_bow()
    while True:
        corpse = FindType(0x2006, Ground())
        found_corpse += GetFindedList()
        if not corpse:
            break

        NewMoveXY(GetX(corpse), GetY(corpse), True, 1, True)
        tamla()
        if TargetPresent():
            CancelTarget()

        name = GetName(corpse)
        if str(name) in scalp or "Daemon" in str(name) or "Fiend" in str(name):
            start_time = datetime.now()
            UseType2(skinning_Knife)
            WaitTargetObject(corpse)
            Wait(1000)
            if InJournalBetweenTimes("You are already doing something else.", start_time, datetime.now()) != -1:
                Wait(2000)
                UseType2(skinning_Knife)
                WaitTargetObject(corpse)
                Wait(1000)
            hides()    

        print(f'Looting: {str(name)}')
        UseObject(corpse)
        if not GetMaxMana(Self()):
            if WarMode() == True:
                SetWarMode(False)
            UseSkill("Meditation")

        for i in loot:
            while FindTypeEx(i, 0xFFFF, corpse, False) > 0:
                item = FindItem()
                start_time = datetime.now()
                MoveItem(item, -1, hunt_pack, 0, 0, 0)
                if InJournalBetweenTimes("You are already holding the item", start_time, datetime.now()) != -1:
                    Disconnect()
                tamla()
                if FindType(zulucoin, Backpack()):
                    MoveItem(FindItem(), FindFullQuantity(), hunt_pack, 0, 0, 0)
                    Wait(100)

        Ignore(corpse)
        main_attack()
    befor_hunt()