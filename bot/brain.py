from staff import name,msg_crafter,msg_hunter,warrior_name,mage_name,scalp,loot,hunt_pack,zulucoin,hide,skinning_Knife
from cast_healing import tamla
from cheking import dead,befor_hunt,zulucoin,medit,hides
from dress import take_kryss,take_bow
from datetime import datetime
from py_stealth import *

def main_attack():
    found = []
    dis_found = []
    SetFindDistance(8)
    for npc in name:
        if FindType(npc, Ground()):
            found += GetFindedList()
            Ignore(npc)
            
    for npc in found:
        if str(GetName(npc)) == "a Mage Hunter":
            print("Mage Hunter")
            take_bow()
            SetWarMode(True)
            NewMoveXY(GetX(npc)+6,GetY(npc)-6,True,1,True)
            while GetHP(npc) > 0:
                print(f"Index: {found.index(npc)}, Name: {str(GetName(npc))}, Distance: {GetDistance(npc)}")
                Attack(npc)
                NewMoveXY(GetX(npc)+6,GetY(npc)-6,True,1,True)
                tamla()
                dead()
                while Paralyzed():
                    print("Paralyzed")
                    NewMoveXY(GetX(npc)+6,GetY(npc)-6,True,1,True)
                    NewMoveXY(GetX(npc)+6,GetY(npc)-6,True,1,True)
                    tamla()
    
    for npc in found:
        if str(GetName(npc)) == "a Lesser Shadow":
            print("a Lesser Shadow")
            Disarm()
            SetWarMode(False)
            NewMoveXY(GetX(npc)+4,GetY(npc)+4,True,1,True)
            while GetHP(npc) > 0:
                print(f"Index: {found.index(npc)}, Name: {str(GetName(npc))}, Distance: {GetDistance(npc)}")
                NewMoveXY(GetX(npc)+4,GetY(npc)+4,True,1,True)
                start_time = datetime.now()
                CastToObject("chain lightning",npc)
                Wait(2000)
                if InJournalBetweenTimes("I can't see that.",start_time,datetime.now()) != -1:
                    NewMoveXY(GetX(npc)-4,GetY(npc)-4,True,1,True)
                tamla()
                dead()
                while Paralyzed():
                    print("Paralyzed")
                    NewMoveXY(GetX(npc)+4,GetY(npc)+4,True,1,True)
                    NewMoveXY(GetX(npc)+4,GetY(npc)+4,True,1,True)
                    tamla()
    
    for npc in found:
        if "Undead" in str(GetName(npc)) or "Dracoliche" in str(GetName(npc)):
            take_bow()
            SetWarMode(True)
            while GetHP(npc) > 0:
                take_bow()
                Attack(npc)
                CastToObject("resurrection",npc)
                NewMoveXY(GetX(npc)-4,GetY(npc)+4,True,1,True)
                tamla()
                dead()
                while Paralyzed():
                    NewMoveXY(GetX(Self())-4,GetY(Self())-4,True,1,True)
                    NewMoveXY(GetX(Self())+3,GetY(Self())-3,True,1,True)

    for npc in found:
        for i in mage_name:
            while i in str(GetName(npc)):
                take_bow()
                SetWarMode(True)
                NewMoveXY(GetX(npc)-4,GetY(npc)-4,True,1,True)
                while GetHP(npc) > 0:
                    print(f"Index: {found.index(npc)}, Name: {str(GetName(npc))}, Distance: {GetDistance(npc)}")
                    Attack(npc)
                    if GetMana(Self()) > 50:
                        start_time = datetime.now()
                        CastToObject("chain lightning",npc)
                        print("lightning")
                        Wait(2000)
                        if InJournalBetweenTimes("I can't see that",start_time,datetime.now()) != -1:
                            print("Moving to another place")
                            NewMoveXY(GetX(npc)+4,GetY(npc)+4,True,1,True)
                        Attack(npc)
                    else: pass
                    NewMoveXY(GetX(npc)-4,GetY(npc)-4,True,1,True)
                    tamla()
                    dead()
                    while Paralyzed():
                        print("Paralyzed")
                        NewMoveXY(GetX(npc)-4,GetY(npc)-4,True,1,True)
                        NewMoveXY(GetX(npc)-4,GetY(npc)-4,True,1,True)
                        tamla()
                break

    for npc in found:    
        for i in warrior_name:
            if i in str(GetName(npc)):
                take_kryss()
                SetWarMode(True)
                Attack(npc)
                NewMoveXY(GetX(npc),GetY(npc),True,1,True)
                while GetHP(npc) > 0:
                    print(f"Number: {found.index(npc)}, Name: {str(GetName(npc))}, Distance: {GetDistance(npc)}")
                    Attack(npc)
                    NewMoveXY(GetX(npc),GetY(npc),True,1,True)
                    tamla()
                    dead()
                    while Paralyzed():
                        print("Paralyzed")
                        NewMoveXY(GetX(Self())-4,GetY(Self())-4,True,1,True)
                        NewMoveXY(GetX(Self())+6,GetY(Self())-6,True,1,True)
                        NewMoveXY(GetX(npc),GetY(npc),True,1,True)
                        tamla()
                        
    main_loot()
    befor_hunt()
    
"""def find_corpse():
    found = []
    SetFindDistance(10)
    for corpse in [0x2006]:
        FindType(corpse,Ground())
        corpseID = FindItem()
        found = corpseID
        found += GetFindedList()
    return found"""

def main_loot():
    SetFindDistance(10)
    take_bow()
    while FindType(0x2006,Ground()) > 0:
        corpse = FindItem()
        NewMoveXY(GetX(corpse),GetY(corpse),True,1,True)
        tamla()
        if TargetPresent():
            CancelTarget()
        if str(GetName(corpse)) in scalp or "Daemon" in str(GetName(corpse)) or "Fiend" in str(GetName(corpse)):
            start_time = datetime.now()
            UseType2(skinning_Knife)
            WaitTargetObject(corpse)
            Wait(1000)
            hides()
            if InJournalBetweenTimes("You are already doing something else.", start_time, datetime.now()) != -1:
                Wait(2000)
                UseType2(skinning_Knife)
                WaitTargetObject(corpse)
                Wait(1000)
                hides()
                 
        print(f'Лутаю: {str(GetName(corpse))}')
        UseObject(corpse)
        if GetMaxMana(Self()):
            pass
        else:
            SetWarMode(False)
            UseSkill("Meditation")
        if FindType(zulucoin,Backpack()):
            MoveItem(FindItem(),FindFullQuantity(),hunt_pack,0,0,0)
            Wait(500)
        for i in loot:
            start_time = datetime.now()
            while FindTypeEx(i,0xFFFF,corpse,False) > 0:
                MoveItem(FindItem(),-1,hunt_pack,0,0,0)
                Wait(10)
                if InJournalBetweenTimes("You are already holding the item", start_time, datetime.now()) != -1:
                    Disconnect()
                else:
                    pass
                tamla()
                if FindType(zulucoin,Backpack()):
                    MoveItem(FindItem(),FindFullQuantity(),hunt_pack,0,0,0)
                    Wait(500)
            Ignore(corpse)
        main_attack()
        main_loot()
        
    befor_hunt()

"""def hides():
    for i in hide:
        if FindType(i,Backpack()):
            MoveItem(FindItem(),FindFullQuantity(),hunt_pack,0,0,0)
            Wait(500)"""
           

        
