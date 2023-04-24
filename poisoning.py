from py_stealth import *
from datetime import *
import timeit

item = 0x66E8

def itemID():
    FindType(item,Backpack())
    UseSkill("Item Identification")
    WaitTargetObject(FindItem())
    Wait(5000)
    
if __name__== "__main__":
    while True:
        itemID()