from py_stealth import *
from datetime import *
import timeit

dagger = 0x0F51
chisel = 0x1026
tool = 0x1035
wood = 0x1BDD
item_skill_110 = 0x0DF0
item_skill_100 = 0x65CA 
item_skill_95 = 0x66A4
box = 0x53DDDB89
msg = "Legendary"

def pereplav():
    if GetSkillValue("Carpentry") >= 90 and GetSkillValue("Carpentry") < 95:
        while FindType(item_skill_95,Backpack()):
            UseType(chisel,0xFFFF)
            WaitTargetObject(FindType(item_skill_95,Backpack()))
            Wait(500)
            TargetToObject(Self())
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You turned",10000)
    
    elif GetSkillValue("Carpentry") >= 95 and GetSkillValue("Carpentry") < 119:
        while FindType(item_skill_100,Backpack()):
            UseType(chisel,0xFFFF)
            WaitTargetObject(FindType(item_skill_100,Backpack()))
            Wait(500)
            TargetToObject(Self())
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You turned",10000)
            
    elif GetSkillValue("Carpentry") >= 120:
        while FindType(item_skill_110,Backpack()):
            UseType(chisel,0xFFFF)
            WaitTargetObject(FindType(item_skill_110,Backpack()))
            Wait(500)
            TargetToObject(Self())
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You turned",10000)

def checklegendery():
    if GetSkillValue("Carpentry") < 120:
        pereplav()
    else:
        if FindType(item_skill_110,Backpack()): 
            if (GetCliloc(FindItem())[46:53]) == msg:
                print("This Item Is Legendery :)")
                MoveItem(FindItem(),1,box,0,0,0)
                print("The Legendery Item In The Box Now.")
            else:
                print("This Item Is not Legendery.")
                print("Destroy This Trash!!!")
                pereplav()
                
        else: print("There is No Item To Check For")

def carp():
    CloseSimpleGump(-1)
    if GetSkillValue("Carpentry") >= 90 and GetSkillValue("Carpentry") < 95:
        if FindType(tool,Backpack()):
            UseType2(tool)
            if FindType(wood,Backpack()):
                WaitTargetObject(FindItem())
                Wait(500)
                WaitGump(400)
                Wait(500)
                WaitGump(55702)
                starttime = datetime.now()
                WaitJournalLineSystem(starttime,"You finish",10000)
                Wait(500)
            else:
                print("There Is No Wood In Your Backpack.")
                
    elif GetSkillValue("Carpentry") >= 95 and GetSkillValue("Carpentry") < 120:
        if FindType(tool,Backpack()):
            UseType2(tool)
            if FindType(wood,Backpack()):
                WaitTargetObject(FindItem())
                Wait(500)
                WaitGump(400)
                Wait(500)
                WaitGump(55607) 
                starttime = datetime.now()
                WaitJournalLineSystem(starttime,"You finish",10000)
                Wait(500)
            else:
                print("There Is No Wood In Your Backpack.")
            
    elif GetSkillValue("Carpentry") >= 120:
        if FindType(tool,Backpack()):
            UseType2(tool)
            if FindType(wood,Backpack()):
                WaitTargetObject(FindItem())
                Wait(500)
                WaitGump(400)
                Wait(500)
                WaitGump(3568) 
                starttime = datetime.now()
                WaitJournalLineSystem(starttime,"You finish",10000)
                Wait(500)
            else:
                print("There Is No Wood In Your Backpack.")
    else:
        print("There Is No Tool's Anymore.")
        Wait(1000)
       
def armsLore():
    if FindType(dagger,Backpack()) > 0:
        UseSkill('Arms Lore')
        WaitTargetObject(FindItem())
        Wait(500)
    else:
        print("There Is Nothing To Lore.")
        Wait(1000)

def checkLogAmount():
    return(print(f'Осталось {str(CountEx(wood, 0xFFFF, Backpack()))} дерево в паке. Carpentry: {GetSkillValue("Carpentry")}'))


def main():
    carp()
    armsLore()
    ClearSystemJournal()
    checklegendery()
    checkLogAmount()
    
   
if __name__ == '__main__':
    while (True):
        main()