from staff import bow,bowID

from py_stealth import *

def take_bow():
    if FindType(bow,Backpack()):
        Disarm()
        Wait(1000)
        print("Bow")
        Equip(1,bowID)
        Wait(200)