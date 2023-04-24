from py_stealth import *
from datetime import *
import timeit
from datetime import datetime
from staff import *


def main_attack():
    found = []
    SetFindDistance(15)
    for npc in name:
        if FindType(npc, Ground()):
            found += GetFindedList()
            Ignore(npc)
    for npc in found:
        if "Undead" in str(GetName(npc)) or "Dracoliche" in str(GetName(npc)):
            take_bow()
            SetWarMode(True)
            while GetHP(npc) > 0:
                take_bow()
                SetWarMode(False)
                SetWarMode(True)
                Attack(npc)
                CastToObject("resurrection",npc)
                NewMoveXY(GetX(npc)-4,GetY(npc)+4,True,1,True)
                tamla()
                Wait(2200)
                check_dead()
                while Paralyzed():
                    NewMoveXY(GetX(Self())-4,GetY(Self())-4,True,1,True)
                    NewMoveXY(GetX(Self())+3,GetY(Self())-3,True,1,True)

    
    for npc in found:
        for i in mage_name:
            if i in str(GetName(npc)):
                print("Take_bow")
                take_bow()
                SetWarMode(True)
                NewMoveXY(GetX(npc)-3,GetY(npc)-3,True,1,True)
                while GetHP(npc) > 0:
                    print(f"Number: {found.index(npc)}, Name: {str(GetName(npc))}, Distance: {GetDistance(npc)}")
                    SetWarMode(False)
                    SetWarMode(True)
                    Attack(npc)
                    if GetMana(Self()) > 50:
                        CastToObject("chain lightning",npc)
                        Attack(npc)
                    else: pass
                    NewMoveXY(GetX(npc)-3,GetY(npc)-3,True,1,True)
                    tamla()
                    check_dead()
                    while Paralyzed():
                        print("Paralyzed")
                        NewMoveXY(GetX(Self())-3,GetY(Self())-3,True,1,True)
                        NewMoveXY(GetX(Self())+3,GetY(Self())-3,True,1,True)
                        tamla()

    for npc in found:    
        for i in warrior_name:
            if i in str(GetName(npc)):
                take_kryss()
                SetWarMode(True)
                Attack(npc)
                NewMoveXY(GetX(npc),GetY(npc),True,1,True)
                while GetHP(npc) > 0:
                    print(f"Number: {found.index(npc)}, Name: {str(GetName(npc))}, Distance: {GetDistance(npc)}")
                    SetWarMode(False)
                    SetWarMode(True)
                    Attack(npc)
                    NewMoveXY(GetX(npc),GetY(npc),True,1,True)
                    tamla()
                    check_dead()
                    while Paralyzed():
                        print("Paralyzed")
                        NewMoveXY(GetX(Self())-4,GetY(Self())-4,True,1,True)
                        NewMoveXY(GetX(Self())+6,GetY(Self())-6,True,1,True)
                        NewMoveXY(GetX(npc),GetY(npc),True,1,True)
                        tamla()

    

    medit()
    main_loot()
    check_befor_hunt()
    
def find_corpse():
    found = []
    SetFindDistance(10)
    for corpse in [0x2006]:
        FindType(corpse,Ground())
        corpseID = FindItem()
        found = corpseID
        found += GetFindedList()
    return found

def main_loot():
    SetFindDistance(10)
    take_bow()
    while FindType(0x2006,Ground()) > 0:
        corpse = FindItem()
        NewMoveXY(GetX(corpse),GetY(corpse),True,1,True)
        tamla()
        if TargetPresent():
            CancelTarget()
        if str(GetName(corpse)) in scalp or "Daemon" in str(GetName(corpse)):
            UseType2(skinning_Knife)
            WaitTargetObject(corpse)
            Wait(1000)
            check_hides()
        
        print(f'Имя трупа: {str(GetName(corpse))}')
        UseObject(corpse)
        if GetMaxMana(Self()):
            pass
        else:
            SetWarMode(False)
            UseSkill("Meditation")
        check_zulucoin()
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
            Ignore(corpse)
        
        main_loot()
        main_attack()
    check_befor_hunt()

def tamla():
    if GetHP(Self()) < 250:
        if FindTypeEx(bottle,tamla_color,hunt_pack,False):
            UseObject(FindItem())

####### Recalls

def buy_horse():
    print("buy_horse")
    SetFindDistance(5)
    FindTypeEx(gold,0xFFFF,ObjAtLayer(BankLayer()))
    MoveItem(FindItem(),320,Backpack(),0,0,0)
    Wait(1000)
    if FindType(gold,Backpack()) >= 320:
        UseObject(runebook)
        WaitGump(1042)
        Wait(5000)
        if str(PredictedX()) != "4438" and str(PredictedY()) != "1179":
            print(f"{PredictedX()} {PredictedY()}")
            buy_horse()

        UOSay("buy")
        Wait(1000)
        AutoBuy(0x2120,0xFFFF,1)
        Wait(1000)
        FindType(horse,Ground())
        NewMoveXY(GetX(FindItem()),GetY(FindItem()),True,1,True)
        UseObject(FindItem())
    else:
        print("buy_horse: Else")
        
def recall_to_minoc_undead():
    UseObject(runebook)
    WaitGump(1034)
    Wait(5000)
    if str(PredictedX()) != "2468" and str(PredictedY()) != "1111":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_minoc_undead()
    else:
        pass
        
def recall_to_spellbook_vozle_doma():
    Cast("polymorph")
    Wait(2000)
    check_befor_hunt()
    UseObject(runebook)
    WaitGump(1045)
    Wait(5000)
    main_attack()
    Wait(1000)
    check_befor_hunt()
    main_attack()
        
def recall_to_ebooki():
    Cast("polymorph")
    Wait(2000)
    check_befor_hunt()
    UseObject(runebook)
    WaitGump(1046)
    Wait(5000)
    main_attack()
    Wait(1000)
    check_befor_hunt()
    main_attack()

   
def recall_to_spellbook_0():
    check_befor_hunt()
    UseObject(runebook)
    WaitGump(1027)
    Wait(5000)
    if str(PredictedX()) != "1216" and str(PredictedY()) != "660":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_spellbook_0()
    else:
        Cast("polymorph")
        with open('location/spellbooks_0.txt') as f:
            tile = f.readlines()
            for line in tile:
                NewMoveXY(line[7:11],line[12:16],True,1,True)
                main_attack()
                Wait(1000)
                check_befor_hunt()
                main_attack()
                if check_cast():
                    recall_to_spellbook_0()
        with open('next_spellbook.txt') as f:
            tile = f.readlines()
            for line in tile:
                NewMoveXY(line[7:11],line[12:16],True,1,True)
                main_attack()
                check_befor_hunt()
                main_attack()
    
def recall_to_spellbook_minoc_grave():
    check_befor_hunt()
    UseObject(runebook)
    WaitGump(1028)
    Wait(5000)
    if str(PredictedX()) != "2712" and str(PredictedY()) != "796":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_spellbook_minoc_grave()
    else:
        Cast("polymorph")
        with open('location/SB_Minoc_Grave.txt') as f:
            tile = f.readlines()
            for line in tile:
                NewMoveXY(line[7:11],line[12:16],True,1,True)
                main_attack()
                check_befor_hunt()
                main_attack()
                if check_cast():
                    recall_to_spellbook_minoc_grave()

    
def recall_to_spellbook_1():
    check_befor_hunt()
    UseObject(runebook)
    WaitGump(1029)
    Wait(5000)
    if str(PredictedX()) != "3010" and str(PredictedY()) != "694":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_spellbook_1()
    else:
        Cast("polymorph")
        with open('location/SB_1.txt') as f:
            tile = f.readlines()
            for line in tile:
                NewMoveXY(line[7:11],line[12:16],True,1,True)
                main_attack()
                check_befor_hunt()
                main_attack()
                if check_cast():
                    recall_to_spellbook_1()

def recall_to_spellbook_2():
    check_befor_hunt()
    UseObject(runebook)
    WaitGump(1043)
    Wait(5000)
    if str(PredictedX()) != "2283" and str(PredictedY()) != "1095":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_spellbook_1()
    else:
        Cast("polymorph")
        with open('location/spellbook_2.txt') as f:
            tile = f.readlines()
            for line in tile:
                NewMoveXY(line[7:11],line[12:16],True,1,True)
                main_attack()
                check_befor_hunt()
                main_attack()
                if check_cast():
                    recall_to_spellbook_2()
        
def recall_to_undead_trinsic():
    check_befor_hunt()
    UseObject(runebook)
    WaitGump(1036)
    Wait(5000)
    if str(PredictedX()) != "1018" and str(PredictedY()) != "2713":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_undead_trinsic()
    else:
        Cast("polymorph")
        with open('location/undead_trinsic.txt') as f:
            tile = f.readlines()
            for line in tile:
                NewMoveXY(line[7:11],line[12:16],True,1,True)
                main_attack()
                check_befor_hunt()
                main_attack()
                if check_cast():
                    recall_to_undead_trinsic()

def recall_to_spellbook_pook():
    check_befor_hunt()
    UseObject(runebook)
    WaitGump(1037)
    Wait(5000)
    if str(PredictedX()) != "2707" and str(PredictedY()) != "1043":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_spellbook_pook()
    else:
        Cast("polymorph")
        with open('location/spellbooks_pook.txt') as f:
            tile = f.readlines()
            for line in tile:
                NewMoveXY(line[7:11],line[12:16],True,1,True)
                main_attack()
                check_befor_hunt()
                main_attack()
                if check_cast():
                    recall_to_spellbook_pook()

def recall_to_spellbook_minocM():
    check_befor_hunt()
    UseObject(runebook)
    WaitGump(1038)
    Wait(5000)
    if str(PredictedX()) != "2613" and str(PredictedY()) != "82":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_spellbook_minocM()
    else:
        Cast("polymorph")
        with open('location/spellbook_minocM.txt') as f:
            tile = f.readlines()
            for line in tile:
                NewMoveXY(line[7:11],line[12:16],True,1,True)
                main_attack()
                check_befor_hunt()
                main_attack()
                if check_cast():
                    recall_to_spellbook_minocM()

def recall_to_spellbook_brit_0():
    check_befor_hunt()
    UseObject(runebook)
    WaitGump(1040)
    Wait(5000)
    if str(PredictedX()) != "1276" and str(PredictedY()) != "1319":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_spellbook_brit_0()
    else:
        Cast("polymorph")
        with open('location/spellbook_brit_0.txt') as f:
            tile = f.readlines()
            for line in tile:
                NewMoveXY(line[7:11],line[12:16],True,1,True)
                main_attack()
                check_befor_hunt()
                main_attack()
                if check_cast():
                    recall_to_spellbook_brit_0()

def recall_to_liches_0():
    UseObject(runebook)
    WaitGump(1039)
    Wait(5000)
    if str(PredictedX()) != "2625" and str(PredictedY()) != "1105":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_liches_0()
    else:
        pass

def recall_to_Market():
    print("recall_to_Market")
    UseObject(runebook)
    WaitGump(1025)
    Wait(5000)
    if str(PredictedX()) != "2130" and str(PredictedY()) != "804":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_Market()
    else:
        pass

def recall_to_Home():
    UseObject(runebook)
    WaitGump(1031)
    Wait(5000)
    if str(PredictedX()) != "2846" and str(PredictedY()) != "173":
        print(f"{PredictedX()} {PredictedY()}")
        recall_to_Home()
    else:
        pass

def go_to_cast():
    recall_to_Home()
    MoveXYZ(2842,174,6,True,1,True)
    MoveXYZ(2844,172,26,True,1,True)
    UOSay("cast me")
    go_to_unload()
    UseSkill("Meditation")
    load()
    charge_runebook()
    charge_runebook()
    take_bow()
    Wait(1000)
    UOSay("Let's Go to Hunt Some Bustards!")

def charge_runebook():
    SetFindDistance(10)
    FindType(recall_Scrolls,Ground())
    print(f"взял с пола {str(CountEx(recall_Scrolls,0xFFFF,Ground()))} рекол скролов.")
    MoveXYZ(2846,175,26,True,1,True)
    Grab(FindItem(),FindFullQuantity())
    Wait(300)
    if FindType(recall_Scrolls,Backpack()):
        MoveItem(FindItem(),FindFullQuantity(),runebook,GetX(runebook),GetY(runebook),GetZ(runebook))
        startime = datetime.now()
        WaitJournalLineSystem(startime,"You put|runebook is fully charged.",1000)
    Wait(1500)
    FindType(recall_Scrolls,Backpack())
    DropHere(FindItem())
    Wait(200)

####### Craft

def go_to_repair_kryss():
    Disarm()
    MoveXYZ(2851,174,26,True,1,True)
    UseObject(box)
    FindType(hammer,box)
    Grab(FindItem(),1)
    Wait(200)
    UseType2(hammer)
    Wait(200)
    if FindTypeEx(ingots,deadra,box,True):
        Grab(FindItem(),100)
    Wait(200)
    if TargetPresent():
        CancelTarget()
    MoveXYZ(2852,176,26,True,1,True)
    UseType2(hammer)
    Wait(200)
    FindType(kryss)
    WaitTargetObject(FindItem())
    WaitGump(161)
    Wait(3000)
    MoveXYZ(2849,174,26,True,1,True)
    Disarm()
    Wait(500)
    UseObject(box)
    FindType(hammer,Backpack())
    MoveItem(FindItem(),1,box,0,0,0)
    Wait(500)
    FindType(ingots,Backpack())
    MoveItem(FindItem(),-1,box,0,0,0)
    Wait(500)
    
    

def go_to_repair_bow():
    Disarm()
    MoveXYZ(2849,17,26,True,1,True)
    if TargetPresent():
        CancelTarget()
    UseObject(box)
    Wait(200)
    FindType(hammer,box)
    Wait(200)
    MoveItem(FindItem(),1,Backpack(),0,0,0)
    Wait(500)
    UseType2(hammer)
    FindTypeEx(logs,zulu_color,box,False)
    MoveItem(FindItem(),100,Backpack(),0,0,0)
    Wait(500)
    MoveXYZ(2852,176,26,True,1,True)
    UseType2(hammer)
    FindType(bow,Backpack())
    WaitTargetObject(FindItem())
    WaitGump(161)
    Wait(3000)
    MoveXYZ(2849,174,26,True,1,True)
    Disarm()
    Wait(500)
    UseObject(box)
    FindType(hammer,Backpack())
    MoveItem(FindItem(),1,box,0,0,0)
    Wait(500)
    FindType(logs,Backpack())
    MoveItem(FindItem(),FindFullQuantity(),box,0,0,0)
    Wait(500)
    

####### Change Classes

def change_class_to_crafter():
    NewMoveXY(2130,847,True,1,True)
    UseObject(0x51BB0D3A)
    WaitGump(7)
    Wait(5000)

def change_class_to_hunter():
    NewMoveXY(2130,847,True,1,True)
    UseObject(0x51BB0D3A)
    WaitGump(6)
    Wait(5000)

def change_class_to_warrior():
    NewMoveXY(2130,847,True,1,True)
    UseObject(0x51BB0D3A)
    WaitGump(1)
    Wait(5000)

def check_class():
    start = datetime.now()
    UOSay(".showclasse")
    Wait(500)
    if InJournalBetweenTimes(msg_hunter, start, datetime.now()) != -1:
        print("Class is Hunter.")
 
    if InJournalBetweenTimes(msg_warrior, start, datetime.now()) != -1:
        print("Class is Warrior.")

    if InJournalBetweenTimes(msg_crafter, start, datetime.now()) != -1:
        print("Class is Crafter.")

#######

####### Dress

def take_bow():
    if FindType(bow,Backpack()):
        Disarm()
        Wait(1000)
        print("Bow")
        Equip(1,bowID)
        Wait(200)

        
def take_kryss():
    if FindType(kryss,Backpack()):
        Disarm()
        Wait(500)
        print("Kryss")
        Equip(1,kryssID)
        Wait(200)

def take_shield_and_kryss():
    Disarm()
    Wait(1000)
    if FindType(kryss,Backpack()):
        print("Kryss")
        Equip(1,kryssID)
        Wait(200)
    if FindType(shield,Backpack()):
        print("Shield")
        Equip(2,shieldID)
        Wait(200)

####### Hidding

def go_hide():
    #Disarm()
    Wait(500)
    Cast("magic reflection")
    Wait(1300)
    SetWarMode(False)
    UseSkill("Hiding")
    Wait(10000)
    if Hidden():
        UseSkill("Stealth")
    else:
        UseSkill("Hiding")
        Wait(10000)
        if Hidden():
            UseSkill("Stealth")
#######

####### Meditation

def medit():
    if GetMana(Self()) < 200:
        start_time = datetime.now()
        SetWarMode(False)
        UseSkill("Meditation")
        Wait(500)
        if InJournalBetweenTimes("I am already performing another action.",start_time,datetime.now()) != -1:
            pass
        else:
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You are already doing something else.|You stop meditating.|You moved and lost your concetration.",10000)
        

####### Healing

def heal():
    while GetHP(Self()) < 250:
        CastToObject("greater heal",Self())
        Wait(1500)

####### Dungeon

def go_to_wrong():
    #recall_to_Market()
    SetFindDistance(10)
    NewMoveXY(2128,828,True,1,True)
    UOSay("Wrong")

def go_to_despice():
    check_befor_hunt()
    recall_to_Market()
    NewMoveXY(2128,829,True,1,True)
    UOSay("Despise")
    Wait(2000)
    Cast("polymorph")
    with open('despice.txt') as f:
        tile = f.readlines()
        for line in tile:
            NewMoveXY(line[7:11],line[12:16],True,1,True)
            main_attack()
            check_befor_hunt()

def go_to_hytloth():
    NewMoveXY(2132,829,True,1,True)
    UOSay("hytloth")
    Wait(2000)

####### Unload

def go_to_unload():
    MoveXYZ(2849,173,26,True,1,True)
    UseObject(sunduk)
    EmptyContainer(hunt_pack,sunduk,500)

####### Load

def load():
    regi = [BP(),BM(),GA(),GS(),MR(),NS(),SA(),SS()]
    thousand = 1000
    hundred = 100
    MoveXYZ(2849,173,26,True,1,True)
    UseObject(sunduk)
    #FindType(arrows,Backpack())
    #MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
    FindTypeEx(arrows,ice_color,Backpack(),False)
    if FindFullQuantity() < thousand:
        print(f"Amount of Fire Arrows in Backpack: {FindFullQuantity()}.")
        result = thousand - FindFullQuantity()
        FindTypeEx(arrows,ice_color,sunduk,False)
        MoveItem(FindItem(),result,hunt_pack,0,0,0)
        Wait(500)
        
    FindType(bandages,Backpack())
    if FindFullQuantity() < thousand:
        print(FindFullQuantity())
        result = thousand - FindFullQuantity()
        FindType(bandages,sunduk)
        MoveItem(FindItem(),result,hunt_pack,0,0,0)
        Wait(500)
    for i in regi:
        FindType(i,Backpack())
        if FindFullQuantity() < hundred:
            result = hundred - FindFullQuantity()
            FindType(i,sunduk)
            MoveItem(FindItem(),result,hunt_pack,0,0,0)
            Wait(500)
    FindType(fish,Backpack())
    if FindFullQuantity() < 20:
        result = 20 - FindFullQuantity()
        FindType(fish,sunduk)
        MoveItem(FindItem(),result,Backpack(),0,0,0)
        Wait(500)
    FindTypeEx(bottle,tamla_color,sunduk,False)
    if FindFullQuantity() > 10:
        FindTypeEx(bottle,tamla_color,hunt_pack,False)
        result = 10 - FindFullQuantity()
        FindTypeEx(bottle,tamla_color,sunduk,False)
        MoveItem(FindItem(),result,hunt_pack,0,0,0)
            
    

def check_zulucoin():
    if FindType(zulucoin,Backpack()):
        MoveItem(FindItem(),FindFullQuantity(),hunt_pack,0,0,0)
        Wait(500)

def check_hides():
    for i in hide:
        FindType(i,Backpack())
        MoveItem(FindItem(),FindFullQuantity(),hunt_pack,0,0,0)
        Wait(500)

def check_arrows():
    t = 1000
    FindTypeEx(arrows,ice_color,Backpack(),False)
    if FindFullQuantity() < 1000:
        if FindTypeEx(arrows,ice_color,hunt_pack,False):
            Grab(FindItem(),Backpack())
        

####### Journal manipulation

def scanJournal():
   start = datetime.now()
   Wait(5000)
   if InJournalBetweenTimes('Hello', start, datetime.now()) != -1:
       AddToSystemJournal('Matching words')
   else:
       AddToSystemJournal('Not a match')

####### Resurrect


def resurrect():
    print("resurrect")
    UOSay(".rescue")
    Wait(500)
    print("Walking to ressurect my self...")
    NewMoveXY(4248,2915,True,1,True)
    NewMoveXY(4248,2911,True,1,True)
    print(PredictedX())
    print(PredictedY())
    while Dead():
        NewMoveXY(4248,2915,True,1,True)
        NewMoveXY(4248,2911,True,1,True)
    
def check_dead():
    if Dead():
        resurrect()
        recall_to_Market()
        UseSkill("Hiding")
        Wait(1500000)
        search_items()
        equip_items()
        buy_horse()

def search_items():
    print("search_items")
    UOSay("bank")
    Wait(500)
    if FindTypeEx(sumka,0xFFFF,ObjAtLayer(BankLayer()),True):
        _foundList = GetFindedList()
        for _found in _foundList:
            UseObject(_found)
    for item in animal_items:
        MoveItem(item,-1,Backpack(),0,0,0)
        Wait(1000)

def equip_items():
    print("equip_items")
    for item in animal_items:
        UseObject(item)
    if TargetPresent():
        CancelTarget()

####### Hunting

def check_befor_hunt():
    check_dead()
    check_cast()
    take_bow()
    medit()

def check_cast():
    if GetStr(Self()) < 280:
        go_to_cast()
        FindType(recall_Scrolls,Ground())
        print(str(CountEx(recall_Scrolls,0xFFFF,Ground())))
        MoveXYZ(2846,175,26,True,1,True)
        Grab(FindItem(),FindFullQuantity())
        Wait(300)
        if FindType(recall_Scrolls,Backpack()):
            MoveItem(FindItem(),FindFullQuantity(),runebook,GetX(runebook),GetY(runebook),GetZ(runebook))
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You put|runebook is fully charged.",1000)
        Wait(500)
        FindType(recall_Scrolls,Backpack())
        DropHere(FindItem())
        Wait(200)

def go_Hunt():
    start = datetime.now()
    UOSay(".showclasse")
    Wait(1000)
    if InJournalBetweenTimes(msg_hunter, start, datetime.now()) != -1:
        print("Class is Hunter.")
    
    elif InJournalBetweenTimes(msg_crafter, start, datetime.now()) != -1:
        print("Class is Crafter.")
        recall_to_Market()
        change_class_to_hunter()
    else:
        pass

    recall_to_spellbook_0()
    recall_to_spellbook_1()
    recall_to_spellbook_2()
    recall_to_spellbook_minoc_grave()
    recall_to_spellbook_minocM()
    recall_to_spellbook_pook()
    recall_to_spellbook_brit_0()
    recall_to_spellbook_vozle_doma()
    #recall_to_ebooki()
    #go_to_despice()
    #recall_to_undead_trinsic()
    
    """
    recall_to_Market()
    go_to_hytloth()
    with open('hytloth.txt') as f:
        tile = f.readlines()
        for line in tile:
            NewMoveXY(line[7:11],line[12:16],True,1,True)
            main_attack()
            #check_arrows()
            medit()
            Wait(1000)
            main_attack()
        main_attack()
    
    check_cast()
    medit()
    take_bow()
    recall_to_minoc_undead()
    with open('minoc_undead.txt') as f:
        tile = f.readlines()
        for line in tile:
            NewMoveXY(line[7:11],line[12:16],True,1,True)
            main_attack()
            #check_arrows()
            medit()
    
    recall_to_liches_0()
    with open('liches_0.txt') as f:
        tile = f.readlines()
        for line in tile:
            NewMoveXY(line[7:11],line[12:16],True,1,True)
            main_attack()
            #check_arrows()
            medit()
    
    check_cast()
    medit()
    recall_to_Market()
    go_to_wrong()
    with open('wrong.txt') as f:
        tile = f.readlines()
        for line in tile:
            NewMoveXY(line[7:11],line[12:16],True,1,True)
            main_attack()
            #check_arrows()
            medit()
    """
#######

def main():
    start_main = datetime.now()
    SetMoveOpenDoor(True)
    SetMoveCheckStamina(True)
    for i in range(8):
        started = datetime.now()
        print(f"{i+1}-й круг охоты")
        go_Hunt()
        recall_to_Home()
        go_to_unload()
        load()
        charge_runebook()
        ClearSystemJournal()
        print(f"{i+1}-й круг охоты")
        ended = datetime.now()
        res_time = ended - started
        print(res_time)
        print("Начал отдых после охоты.")
        """for i in range(7):
            Wait(60000)
            print(f"прошла {i+1}-я минут отдыха после охоты.")
            FindType(zulucoin,sunduk)
            print(f"Zulu Coin's: {FindFullQuantity()}")"""
            
    go_Hunt()
    recall_to_Market()
    change_class_to_crafter()
    recall_to_Home()
    go_to_repair_kryss()
    go_to_repair_bow()
    recall_to_Market()
    change_class_to_hunter()
    recall_to_Home()
    go_to_unload()
    load()
    ClearSystemJournal()
    end_start = datetime.now()
    res_main = end_start - start_main
    print(f"закончил за: {res_main}")
    print("Начал отдых после охоты.")
    """for i in range(7):
        Wait(60000)
        print(f"прошла {i+1}-я минут отдыха после охоты.")"""


if __name__ == "__main__":
    while True:
        main()

    

        
        
        