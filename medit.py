from py_stealth import *
from datetime import *
import timeit
from datetime import datetime


def medit():
    equip(18,0x568CAA4A)
    Wait(200)
    UseSkill("Meditation")
    Wait(200)
    UnEquip(18)
    Wait(10000)
    
    
if __name__ == "__main__":
    while True:
        medit()
    
    
    
