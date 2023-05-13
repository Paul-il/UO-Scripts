from staff import recall_Scrolls,runebook

from datetime import datetime
from py_stealth import *

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
    while FindType(recall_Scrolls,Backpack()):
        DropHere(FindItem())
        Wait(500)