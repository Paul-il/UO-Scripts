from py_stealth import *
from datetime import *
import timeit
from datetime import datetime

trash = 0x540B3EE1
item = 0x65C9 #KeyRing
color = 0xFFFF
tool = 0x1EBA
ingots = 0x1BF2
lore_item = 0x13FE
x = 2843
y = 177
sumka = 0x5537468C
msg = "Legendary"

def drop_item():
    if FindTypeEx(item,color,Backpack(),0) > 0:
        MoveItem(FindItem(),0,trash,x,y,0)
        Wait(500)

def create_item():
    if FindTypeEx(ingots,color,Backpack(),0) > 5:
        UseType2(tool)
        WaitTargetObject(FindItem())
        Wait(500)
        WaitGump(100)
        Wait(500)
        WaitGump(53320)
        startime = datetime.now()
        WaitJournalLineSystem(startime,"Success.",11000)
        Wait(100)
    else:
        print("There Is Not enough ingots to create Item.")

def check_tool():
    if FindType(tool,Backpack()) < 2:
        if FindTypeEx(ingots,color,Backpack(),0) > 5:
            UseType2(tool)
            WaitTargetObject(ingots)
            Wait(500)
            WaitGump(100)
            Wait(500)
            WaitGump(7866)
            startime = datetime.now()
            WaitJournalLineSystem(startime,"Success.",11000)
        else:
            print("Not enough ingots for tool")
    else:
        pass
            
def armsLore():
    if GetSkillValue("Arms Lore") < 150:
        if FindType(lore_item,Backpack()):
            UseSkill('Arms Lore')
            WaitTargetObject(FindItem())
            Wait(500)
        else:
            print("There Is Nothing To Lore.")
            Wait(1000)
    else: 
        pass

def checklegendery():
    CheckLag(500)
    while FindType(item,Backpack()): 
        if (GetCliloc(FindItem())[0:9]) == msg:
            drop_item()
        else:
            drop_item()
            
    else: print("There is No Item To Check For")

def checkAmount():
    if FindTypeEx(ingots,0xFFFF,Backpack(),0):
        print(f"Осталось {FindFullQuantity()} железа, Tinkering Skill:"+ str(GetSkillValue("Tinkering")))
        
    else:
        print("There is No ingots In Your Backpack.")

def main():
    check_tool()
    create_item()
    armsLore()
    checklegendery()
    ClearSystemJournal()
    checkAmount()
    Wait(1000)
    
    

 

if __name__ == '__main__':
    while (True):
        script_start_time = datetime.now()
        main()
        script_end_time = datetime.now()
        print(script_end_time - script_start_time)
        
    