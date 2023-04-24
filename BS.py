from py_stealth import *
from datetime import *
import timeit
tongs = 0x0FBB
forge = 0x53D54DEE
hammer = 0x13E3
ingots = 0x1BF2
item = 0x5585
box = 0x53DDDB89
msg = "Legendary"
spear = "3939"
kryss = "5121"

def pereplav():
    if FindType(item,Backpack()) > 0:
        UseType(tongs,0xFFFF)
        WaitTargetObject(FindType(item,Backpack()))
        Wait(500)
        WaitTargetObject(forge)
        Wait(2500)

def checklegendery():
    while FindType(item,Backpack()): 
        if msg in (GetCliloc(FindItem())):
            print("This Item Is Legendery :)")
            MoveItem(FindItem(),1,box,0,0,0)
            print("The Legendery Item In The Box Now.")
        else:
            print("This Item Is not Legendery.")
            print("Destroy This Trash!!!")
            pereplav()
            
    else: print("There is No Item To Check For")
        

def bs():
    CloseSimpleGump(-1)
    UseType2(hammer)
    if FindType(ingots,Backpack()):
        WaitTargetObject(FindItem())
        Wait(500)
        WaitGump(300)
        Wait(500)
        WaitGump(3040)
        Wait(500)
        WaitGump(55580) #110 skill
        #WaitGump(55482) # 95 skill
        Wait(7500)
    else:
        print("There Is No Ingos In Your Backpack.")

def checkitem():
    ClearSystemJournal()
    if FindType(item,Backpack()) > 0:
        print(GetName(FindItem()))
    else:
        print("Pass")
       
def armsLore():
    if FindType(item,Backpack()) > 0:
        UseSkill('Arms Lore')
        WaitTargetObject(FindItem())
        Wait(500)
    else:
        print("There Is Nothing To Lore.")
        Wait(1000)

def checkAmount():
    if FindTypeEx(ingots,0xFFFF,Backpack(),0):
        print(f"Осталось {FindFullQuantity()} железа.")
    else:
        print("There is No ingots In Your Backpack.")



def main():
    bs()
    armsLore()
    checklegendery()
    ClearSystemJournal()
    checkAmount()
    
   
if __name__ == '__main__':
    while (True):
        main()