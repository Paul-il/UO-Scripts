from py_stealth import *
from datetime import *
import timeit

sumka = 0x537ACAAC # для руды

def bank():
    NewMoveXY(2507, 520, True, 1, True)  # Bank
    UOSay("Bank")
    CheckLag(10000)

def goback():
    NewMoveXY(2498, 560, True, 1, True)  # Cave   
  
def unload():
    while FindTypesArrayEx([0x19B8, 0x1BF2], [0xFFFF], [Backpack()], False):
        MoveItems(ObjAtLayer(BankLayer()),FindItem(), 0xFFFF, sumka, 0, 0, 0)
        Wait(500)
    #goback()

def main():
	#bank()
    unload()
    
if __name__ == '__main__':
        main()