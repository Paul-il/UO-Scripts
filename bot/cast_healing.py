from staff import bottle,tamla_color,hunt_pack,runebook,recall_Scrolls
from load_unload_staff import load,unload
from dress import take_bow
from datetime import datetime
from py_stealth import *

def tamla():
    if GetHP(Self()) < 250:
        if FindTypeEx(bottle,tamla_color,hunt_pack,False):
            UseObject(FindItem())

def cast():
    if GetStr(Self()) < 320:
        UseObject(runebook)
        WaitGump(1031)
        Wait(5000)
        while str(PredictedX()) != "2846" and str(PredictedY()) != "173":
            print(f"{PredictedX()} {PredictedY()}")
            UseObject(runebook)
            WaitGump(1031)
            Wait(5000)
        UOSay("cast me")
        MoveXYZ(2844,172,26,True,1,True)
        unload()
        SetWarMode(False)
        UseSkill("Meditation")
        load()
        FindType(recall_Scrolls,Ground())
        print(f"{str(CountEx(recall_Scrolls,0xFFFF,Ground()))} Recalls left.")
        MoveXYZ(2846,175,26,True,1,True)
        Grab(FindItem(),FindFullQuantity())
        Wait(300)
        if FindType(recall_Scrolls,Backpack()):
            MoveItem(FindItem(),FindFullQuantity(),runebook,GetX(runebook),GetY(runebook),GetZ(runebook))
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You put|runebook is fully charged.",1000)
        Wait(500)
        while FindType(recall_Scrolls,Backpack()):
            DropHere(FindItem())
            Wait(200)
        take_bow()
        Wait(1000)
        UOSay("Let's Go to Hunt Some Bustards!")
        with open("location/file_cast.txt") as f:
            line = f.readlines()
            if line in ['\n', '\r', '\r\n']:
                pass
            else:
                print(str(line[3]))
                UseObject(runebook)
                WaitGump(line[3])
                Wait(5000)
                NewMoveXY(line[0],line[1],True,1,True)
                
