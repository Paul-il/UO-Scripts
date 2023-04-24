from py_stealth import *
from datetime import *
import timeit
chisel = 0x1026
stol = 0x53D856AB
tool = 0x1022
wood = 0x1BDD
x = 2145                      # Это х тайл
y = 839
color = 0x0000
bow = 0x26C2

def pereplav():
    while FindType(bow,Backpack()) > 0:
        UseType(chisel,0xFFFF)
        WaitTargetObject(FindType(bow,Backpack()))
        Wait(500)
        TargetToObject(Self())
        Wait(2500)


def bowCraft():
    CloseSimpleGump(-1)
    if FindType(tool,Backpack()):
        UseType2(tool)
        if FindType(wood,Backpack()):
            WaitTargetObject(FindItem())
            Wait(500)
            WaitGump(200)
            Wait(500)
            WaitGump(5192)
            Wait(7500)
        else:
            print("There Is No Wood In Your Backpack.")
    else:
        print("There Is No Tool's Anymore.")
        Wait(1000)
       
def armsLore():
    if FindType(bow,Backpack()) > 0:
        UseSkill('Arms Lore')
        WaitTargetObject(FindItem())
        Wait(500)
    else:
        print("There Is Nothing To Lore.")
        Wait(1000)

def checkLogAmount():
    if FindTypeEx(wood,0xFFFF,Backpack(),0):
        print(f"Осталось {FindFullQuantity()} дерево.")
    else:
        print("There is No Wood In Your Backpack.")



def main():
    bowCraft()
    armsLore()
    pereplav()
    ClearSystemJournal()
    checkLogAmount()
    
   
if __name__ == '__main__':
    while (True):
        main()