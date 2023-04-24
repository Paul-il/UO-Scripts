from staff import zulucoin,arrows,ice_color,sumka,animal_items,recall_Scrolls,runebook,gold,horse,hunt_pack,hide
from dress import take_bow
from cast_healing import cast
from load_unload_staff import load,unload
from datetime import datetime
from py_stealth import *


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
    
def dead():
    if Dead():
        resurrect()
        market()
        UseSkill("Hiding")
        for i in range(25):
            Wait(60000)
            print(f"прошло {i+1}")
        search_items()
        equip_items()
        if TargetPresent():
            CancelTarget()
        with open("location/file_cast.txt", 'w+') as f:
            f.readlines()
        buy_horse()

def search_items():
    print("search_items")
    UOSay("bank")
    Wait(500)
    if FindTypeEx(sumka,0xFFFF,ObjAtLayer(BankLayer()),True):
        _foundList = GetFindedList()
        for _found in _foundList:
            UseObject(_found)
    Wait(1000)
    for item in animal_items:
        MoveItem(item,-1,Backpack(),0,0,0)
        Wait(1000)
 

def equip_items():
    print("equip_items")
    for item in animal_items:
        if item == 0x52DC96F2:
            pass
        else:
            UseObject(item)
    if TargetPresent():
        CancelTarget()

####### Hunting

def hides():
    for i in hide:
        if FindType(i,Backpack()):
            MoveItem(FindItem(),FindFullQuantity(),hunt_pack,0,0,0)
            Wait(500)

def befor_hunt():
    dead()
    take_bow()
    medit()

def medit():
    if GetMana(Self()) < 250:
        start_time = datetime.now()
        SetWarMode(False)
        UseSkill("Meditation")
        Wait(500)
        if InJournalBetweenTimes("I am already performing another action.|You are already doing something else.",start_time,datetime.now()) != -1:
            pass
        else:
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You are already doing something else.|You stop meditating.|You moved and lost your concetration.",10000)  
            
def buy_horse():
    UOSay("Bank")
    print("buy_horse")
    SetFindDistance(5)
    if not FindType(gold,hunt_pack):
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
    else:
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

def market():
    print("recall_to_Market")
    UseObject(runebook)
    WaitGump(1025)
    Wait(5000)
    if str(PredictedX()) != "2130" and str(PredictedY()) != "804":
        print(f"{PredictedX()} {PredictedY()}")
        market()
    else:
        pass        
        
def charge_runebook():
    SetFindDistance(10)
    FindType(recall_Scrolls,Ground())
    print(f"взял с пола {str(CountEx(recall_Scrolls,0xFFFF,Ground()))} рекол скролов.")
    MoveXYZ(2846,175,26,True,1,True)
    Grab(FindItem(),FindFullQuantity())
    Wait(1500)
    if FindType(recall_Scrolls,Backpack()):
        MoveItem(FindItem(),FindFullQuantity(),runebook,GetX(runebook),GetY(runebook),GetZ(runebook))
        startime = datetime.now()
        WaitJournalLineSystem(startime,"You put|runebook is fully charged.|charges to the runebook.",1000)
    Wait(1500)
    FindType(recall_Scrolls,Backpack())
    DropHere(FindItem())
    Wait(200)
    
    

