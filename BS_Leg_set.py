from py_stealth import *
from datetime import *
import timeit

tongs = 0x0FBB
forge = 0x53D54DEE
hammer = 0x13E3
ingots = 0x1BF2
tinker_tool = 0x1EBA
citrines = 0x0F15
sun_color = 0x0514
box = 0x53DDDB89
msg = "Legendary"
spear = "3939"
kryss = "5121"

arm_set = {0x6644:"coif",0x663A:"sleevs",0x6643:"leggings",0x6642:"tunic",0x316D:"gorget",0x13F2:"gloves",0x1085:"Necklace",0x1086:"Braclet",0x1087:"Earrings",0x108A:"Ring",0x688E:"Talisman"}

def pereplav():
    for item in arm_set:
        if FindType(item,Backpack()) > 0:
            UseType(tongs,0xFFFF)
            WaitTargetObject(FindType(item,Backpack()))
            Wait(500)
            WaitTargetObject(forge)
            Wait(2500)

def checklegendery():
    for item in arm_set:
        while FindType(item,Backpack()): 
            if msg in (GetCliloc(FindItem())):
                print("This Item Is Legendery :)")
                MoveItem(FindItem(),1,box,0,0,0)
                print("The Legendery Item In The Box Now.")
            else:
                print("This Item Is not Legendery.")
                print("Destroy This Trash!!!")
                pereplav()
                

def create_armor(item_type, box_type, item_value):
    if FindType(box_type, box) >= 2:
        pass
    else:
        CloseSimpleGump(-1)
        UseType2(hammer)
        if FindType(ingots, Backpack()):
            WaitTargetObject(FindItem())
            Wait(500)
            WaitGump(100)
            Wait(500)
            WaitGump(1002)
            Wait(500)
            WaitGump(item_value)
            Wait(7500)
        else:
            print("There are no ingots in your backpack.")

def create_jewelry(item_id, gump_id):
    print(item_id)
    if FindType(item_id, box):
        return
    CloseSimpleGump(-1)
    UseType2(tinker_tool)
    if FindType(ingots, Backpack()):
        WaitTargetObject(FindItem())
        Wait(500)
        WaitGump(600)
        Wait(500)
        WaitGump(gump_id)
        FindType(citrines, Backpack())
        WaitTargetObject(FindItem())
        Wait(7500)
    else:
        print("There Is No Ingots In Your Backpack.")

def bs_coif():
    create_armor(hammer, 0x6644, 56488)

def bs_sleevs():
    create_armor(hammer, 0x663A, 56478)

def bs_leggings():
    create_armor(hammer, 0x6643, 56487)

def bs_tunic():
    create_armor(hammer, 0x6642, 56486)

def bs_gloves():
    create_armor(hammer, 0x13F2, 5106)

def bs_gorget():
    create_armor(hammer, 0x316D, 56194)

def bs_necklace():
    create_jewelry(0x1085, 4229)
    
def bs_braclet():
    create_jewelry(0x1086, 4230)

def bs_earrings():
    create_jewelry(0x1087, 4231)

def bs_ring():
    create_jewelry(0x108A, 4234)

def bs_talisman():
    create_jewelry(0x688E, 56606)
       
def checkitem():
    ClearSystemJournal()
    if FindType(item,Backpack()) > 0:
        print(GetName(FindItem()))
       
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
    try:
        bs_coif()
        checklegendery()
        bs_sleevs()
        checklegendery()
        bs_leggings()
        checklegendery()
        bs_tunic()
        checklegendery()
        bs_gloves()
        checklegendery()
        bs_gorget()
        checklegendery()
        bs_necklace()
        checklegendery()
        bs_braclet()
        checklegendery()
        bs_earrings()
        checklegendery()
        bs_ring()
        checklegendery()
        ClearSystemJournal()
        checkAmount()
    except Exception as e:
        print("An error occurred:", e)   
   
if __name__ == '__main__':
    while (True):
        main()
