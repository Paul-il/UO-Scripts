from staff import name,msg_crafter,msg_hunter,warrior_name,mage_name,scalp,loot,hunt_pack,zulucoin,hide,skinning_Knife
from cast_healing import tamla
from cheking import dead,befor_hunt,zulucoin,medit,hides
from dress import take_kryss,take_bow
from datetime import datetime
from py_stealth import *

def attack_target(npc):
    target_name = str(GetName(npc))
    if target_name == "a Mage Hunter":
        take_bow()
        set_war_mode(True)
        attack_and_move(npc)
    elif target_name == "a Lesser Shadow":
        Disarm()
        set_war_mode(False)
        cast_and_move(npc)
    elif "Undead" in target_name or "Dracoliche" in target_name:
        take_bow()
        set_war_mode(True)
        attack_and_move(npc)
    elif any(i in target_name for i in mage_name):
        take_bow()
        set_war_mode(True)
        attack_and_move(npc)
        if GetMana(Self()) > 50:
            cast_and_move(npc)

def attack_and_move(npc):
    while GetHP(npc) > 0:
        Attack(npc)
        NewMoveXY(GetX(npc) + 6, GetY(npc) - 6, True, 1, True)
        tamla()
        dead()
        while Paralyzed():
            NewMoveXY(GetX(npc) + 6, GetY(npc) - 6, True, 1, True)
            
        tamla()
        main_loot()

def cast_and_move(npc):
    while GetHP(npc) > 0:
        start_time = datetime.now()
        CastToObject("chain lightning", npc)
        Wait(2000)
        if InJournalBetweenTimes("I can't see that.", start_time, datetime.now()) != -1:
            NewMoveXY(GetX(npc) - 4, GetY(npc) - 4, True, 1, True)
        tamla()
        dead()
        while Paralyzed():
            NewMoveXY(GetX(npc) + 4, GetY(npc) + 4, True, 1, True)
            tamla()

def set_war_mode(mode):
    SetWarMode(mode)

def main_attack():
    SetFindDistance(8)
    found = []
    for npc in name:
        if FindType(npc, Ground()):
            found += GetFindedList()
            Ignore(npc)
    for npc in found:
        attack_target(npc)

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
            hides()
        print(f'Looting: {str(name)}')
        UseObject(corpse)
        if not GetMaxMana(Self()):
            SetWarMode(False)
            UseSkill("Meditation")

        for i in loot:
            while FindTypeEx(i, 0xFFFF, corpse, False) > 0:
                item = FindItem()
                start_time = datetime.now()
                MoveItem(item, -1, hunt_pack, 0, 0, 0)
                Wait(10)
                if InJournalBetweenTimes("You are already holding the item", start_time, datetime.now()) != -1:
                    Disconnect()
                tamla()
                if FindType(zulucoin, Backpack()):
                    MoveItem(FindItem(), FindFullQuantity(), hunt_pack, 0, 0, 0)
                    Wait(500)

        Ignore(corpse)
        main_attack()
    befor_hunt()