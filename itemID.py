from py_stealth import *
from datetime import *
import timeit

item = 0x66E8

def itemID():
    UseSkill("Cartography")
    WaitMenu('What', 'World Map')
    Wait(12000)
    
if __name__== "__main__":
    while True:
        itemID()