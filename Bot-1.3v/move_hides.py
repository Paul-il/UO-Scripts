from staff import hide,hunt_pack

from py_stealth import *

def hides():
    for i in hide:
        while FindType(i,Backpack()):
            MoveItem(FindItem(),FindFullQuantity(),hunt_pack,0,0,0)
            Wait(500)