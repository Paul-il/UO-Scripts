from dead import dead
from drink_tamla import tamla
from bow import take_bow

from py_stealth import *
import time
from datetime import datetime

def movement(npc):
    SetWarMode(True)
    Attack(npc)
    NewMoveXY(GetX(npc)+3, GetY(npc)-3, True, 1, True)
    time.sleep(3)
    NewMoveXY(GetX(npc)+4, GetY(npc)+4, True, 1, True)
    time.sleep(3)
    NewMoveXY(GetX(npc)+2, GetY(npc)+2, True, 1, True)
    tamla()
    dead()

def great_wyrm(npc,found):
    pass

def lesser_shadow_tactic(npc, found):
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

def undead_tactic(npc, found):
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

def mage_tactic(npc, found):
    start_time = datetime.now()
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
            time.sleep(2)
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
        
def warrior_tactic(npc, found):
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