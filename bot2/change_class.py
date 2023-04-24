from staff import runebook
from datetime import datetime
from py_stealth import *

def crafter():
    NewMoveXY(2130,847,True,1,True)
    UseObject(0x51BB0D3A)
    WaitGump(7)
    Wait(5000)

def hunter():
    NewMoveXY(2130,847,True,1,True)
    UseObject(0x51BB0D3A)
    WaitGump(6)
    Wait(5000)

def warrior():
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
