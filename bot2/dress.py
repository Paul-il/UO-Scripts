from staff import bow,bowID,kryss,kryssID
from datetime import datetime
from py_stealth import *

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
        Wait(1000)
        print("kryss")
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

