from py_stealth import *
from datetime import *
import timeit
from datetime import datetime
import os

resY = "2545"
resX = "629"
fish = 0x097B
tinkering_tool = 0x1EBA
pickaxe = 0x0E85
ingots = 0x1BF2
ore = 0x19B8
fish_20 = "20"
max_wight = 100
sunduk = 0x56E16687

######### Ore Colors
color = {'Iron':'0x0000','Copper':'0x0602','Black Dwarf':'0x0425','Pagan':'0x050C','Silver':'0x03E9','Spectral':'0x0483','Lavarock':'0x0486','Basilisk':'0x0487'}

######### Fish

def fish_main():
    if str(CountEx(fish, 0xFFFF, Backpack())) < str(1):
        NewMoveXY(2562, 509,True,1,True)
        NewMoveXY(2562, 529,True,1,True)
        go_to_bank()
        move_fish_to_backpack_from_bank()
    else:
        pass

def amount_fish_in_backpack():   # Work
    return(CountEx(fish, 0xFFFF, Backpack()))

def amount_fish_in_bank(): # Work
    return(print(f'{str(CountEx(fish, 0xFFFF, ObjAtLayer(BankLayer())))} рыбы в Багке.'))
    
def move_fish_to_backpack_from_bank(): # Work
    if FindType(fish, ObjAtLayer(BankLayer())):
        FindType(fish,Backpack())
        i = FindFullQuantity()
        if i >= 20:
            pass
        else:
            Grab(FindType(fish, ObjAtLayer(BankLayer())), int(fish_20) - i)
            result = int(fish_20) - i
            print(f'взял с Банка {result}  рыбы.')
            Wait(500)
            print(f'Теперь в паке {str(CountEx(fish, 0xFFFF, Backpack()))} рыбы.')
    else:
        print(f'в Банке осталось {str(CountEx(fish, 0xFFFF, ObjAtLayer(BankLayer())))} рыбы.')
        Wait(500)
#########

######### Tinkering Tools
def amount_of_tinkering_tools_in_bank(): # Work
    return CountEx(tinkering_tool,0xFFFF,ObjAtLayer(BankLayer()))
       
def move_tinkering_tools_to_backpack_from_bank():  # Work
    if FindTypeEx(tinkering_tool,0xFFFF,ObjAtLayer(BankLayer()),False):
        Grab(FindItem(),Backpack())

def make_tinkering_tool_from_bank():
    if amount_of_tinkering_tools_in_bank() < 2:
        if amount_of_ingots_in_bank() > 8:
            move_tinkering_tools_to_backpack_from_bank()
            move_ingots_to_backpack_from_bank()
            Wait(500)
            UseType2(tinkering_tool)
            WaitTargetObject(FindItem())
            Wait(500)
            WaitGump(100)
            Wait(500)
            WaitGump(7866)
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You stop.",25000)
        else:
            print("надо дописать ")
    else:
        print("pass")
#########

######### Pickaxe

def pickaxe_main():
    while str(amount_pickaxe_in_backpack()) < str(2):
        go_to_bank()
        if amount_pickaxe_in_bank():
            move_pickaxe_to_the_backpack_from_bank()
            Wait(500)
            print(f'{str(amount_pickaxe_in_bank())} кирок в Банке')
            print(f'{str(amount_pickaxe_in_backpack())} кирок в паке')
        else:
            make_pickaxe_from_bank()
            move_pickaxe_to_the_chest_from_backpack()

def make_pickaxe_from_bank():
    if FindTypeEx(ingots,0xFFFF,ObjAtLayer(BankLayer()),False) > 40:
        print("начинаю делать кирки.")
        print(str(FindFullQuantity()) + " иногов в Банке.")
        Grab(FindItem(),40)
        Wait(500)
        if FindType(tinkering_tool,Backpack()):
            UseType2(tinkering_tool)
            FindTypeEx(ingots,0xFFFF,Backpack(),False)
            WaitTargetObject(FindItem())
            Wait(500)
            WaitGump(400)
            Wait(500)
            WaitGump(3717)
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You stop.",60000)
        else:
            FindType(tinkering_tool,ObjAtLayer(BankLayer()))
            Grab(FindItem(),1)
            Wait(500)
            if FindType(tinkering_tool,Backpack()):
                UseType2(tinkering_tool)
                FindTypeEx(ingots,0xFFFF,Backpack(),False)
                WaitTargetObject(FindItem())
                Wait(500)
                WaitGump(400)
                Wait(500)
                WaitGump(3717)
                startime = datetime.now()
                WaitJournalLineSystem(startime,"You stop.",60000)
            else:
                make_pickaxe_from_bank()
    else:
        print(str(FindFullQuantity()) + " кирок в Банке.")
        MoveItem(FindItem(), 1,Backpack(), 0, 0, 0)
        Wait(100)
        print(f'{amount_pickaxe_in_backpack()} кирок в сумке')
        
def move_pickaxe_to_the_backpack_from_bank():
    if FindType(pickaxe, ObjAtLayer(BankLayer())):
        Wait(500)
        print("осталос " + str(FindFullQuantity()) + " кирок в Банке.")
        MoveItem(FindItem(), 1, Backpack(),0,0,0)
        Wait(500)

def move_pickaxe_to_the_chest_from_backpack():
    if FindType(pickaxe, Backpack()):
        print("осталос " + str(FindFullQuantity()) + " кирок в паке.")
        MoveItem(FindType(pickaxe,Backpack()), 1, sunduk,0,0,0)
        Wait(500)

def amount_pickaxe_in_bank():
    return(str(CountEx(pickaxe, 0xFFFF, ObjAtLayer(BankLayer()))))

def amount_pickaxe_in_backpack():
    return(str(CountEx(pickaxe, 0xFFFF, Backpack())))
#########

######### Ingots
def amount_of_ingots_in_bank(): # Work
    return (print(f"""Ingots in Bank!
    Iron: {CountEx(ingots,0x0000,ObjAtLayer(BankLayer()))}, Copper: {CountEx(ingots,0x0602,ObjAtLayer(BankLayer()))}, Black Dwarf: {CountEx(ingots,0x0425,ObjAtLayer(BankLayer()))}, Pagan: {CountEx(ingots,0x050C,ObjAtLayer(BankLayer()))}, Silver: {CountEx(ingots,0x03E9,ObjAtLayer(BankLayer()))},
    Spectral: {CountEx(ingots,0x0483,ObjAtLayer(BankLayer()))}, Lavarock: {CountEx(ingots,0x0486,ObjAtLayer(BankLayer()))}, Basilisk: {CountEx(ingots,0x0487,ObjAtLayer(BankLayer()))},"""))

def amount_of_ingots_in_backpack(): # Work
    return (print(f"""Ingots in Backpack!
    Iron: {CountEx(ingots,0x0000,Backpack())}, Copper: {CountEx(ingots,0x0602,Backpack())}, Black Dwarf: {CountEx(ingots,0x0425,Backpack())}, Pagan: {CountEx(ingots,0x050C,Backpack())}, Silver: {CountEx(ingots,0x03E9,Backpack())},
    Spectral: {CountEx(ingots,0x0483,Backpack())}, Lavarock: {CountEx(ingots,0x0486,Backpack())}, Basilisk: {CountEx(ingots,0x0487,Backpack())},"""))
       
def move_ingots_to_backpack_from_bank():  # Work
    if FindTypeEx(ingots,0xFFFF,ObjAtLayer(BankLayer()),False):
        MoveItem(FindItem(),8,Backpack(),0,0,0)
#########

######### Ore

def move_ore_to_bank_from_backpack():  # Work
    while FindTypeEx(ore,0xFFFF,Backpack(),False):
        MoveItem(FindItem(),FindFullQuantity(),ObjAtLayer(BankLayer()),0,0,0)
        
def amount_of_ore_in_bank(): # Work
    return (print(f"Lavarock: {CountEx(ore,0x0486,ObjAtLayer(BankLayer()))}, Icerock: {CountEx(ore,0x04E7,ObjAtLayer(BankLayer()))}, Mythril: {CountEx(ore,0x0492,ObjAtLayer(BankLayer()))},Basilisk: {CountEx(ore,0x0487,ObjAtLayer(BankLayer()))},Sun: {CountEx(ore,0x0514,ObjAtLayer(BankLayer()))},Deadra: {CountEx(ore,0x0494,ObjAtLayer(BankLayer()))},Doom: {CountEx(ore,0x049F,ObjAtLayer(BankLayer()))},New Zulu: {CountEx(ore,0x0488,ObjAtLayer(BankLayer()))},Paradise Gem: {CountEx(ore,0x06FE,ObjAtLayer(BankLayer()))},Hell Gem: {CountEx(ore,0x0ADC,ObjAtLayer(BankLayer()))},Void Gem: {CountEx(ore,0x0B0E,ObjAtLayer(BankLayer()))}."))

def amount_of_ore_in_backpack(): # Work
    return (print(f"Iron: {CountEx(ore,0x0000,Backpack())},Copper: {CountEx(ore,0x0602,Backpack())},Black Dwarf: {CountEx(ore,0x0425,Backpack())},Pagan: {CountEx(ore,0x050C,Backpack())},Silver: {CountEx(ore,0x03E9,Backpack())},Spectral: {CountEx(ore,0x0483,Backpack())}, Lavarock: {CountEx(ore,0x0486,Backpack())}, Icerock: {CountEx(ore,0x04E7,Backpack())}, Mythril: {CountEx(ore,0x0492,Backpack())},Basilisk: {CountEx(ore,0x0487,Backpack())},Sun: {CountEx(ore,0x0514,Backpack())},Deadra: {CountEx(ore,0x0494,Backpack())},Doom: {CountEx(ore,0x049F,Backpack())},New Zulu: {CountEx(ore,0x0488,Backpack())},Paradise Gem: {CountEx(ore,0x06FE,Backpack())},Hell Gem: {CountEx(0x0F2D,0x0ADC,Backpack())},Void Gem: {CountEx(ore,0x0B0E,Backpack())}."))  

def move_ore_to_chest_from_backpack():  # Work
    raringots = [0x0F2D,0x0F21]
    rarcolor = [0x0ADC,0x06FE,0x0B0E]
    while FindTypeEx(ore,0xFFFF,Backpack(),0):
        MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
    if FindTypeEx(0x0F30,0xFFFF,Backpack(),0):
        MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
    if FindTypeEx(0x0F2D,0x0ADC,Backpack(),0):
        MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
    if FindTypeEx(0x0F2D,0x06FE,Backpack(),0):
        MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
    if FindTypeEx(0x0F21,0x0B0E,Backpack(),0):
        MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)

def drop_ore():
    colors = [0x0000,0x0602,0x0425,0x050C,0x0483]
    if Weight() >= 400:
        print("Ушел скидывать руду.")
        for i in colors:
            FindTypeEx(ore,i,Backpack())
            Drop(FindItem(), 0, 0, 0, 0)
            Wait(100)
        NewMoveXY(2562, 509,True,1,True)
        NewMoveXY(2562, 529,True,1,True)
        go_to_bank()
        move_ore_to_bank_from_backpack()

######### Chest

def goToChest():  # Work
    NewMoveXY(1056,1304,True,1,True)
    
def move_ingots_to_backpack_from_chest():  # Work
    if FindTypeEx(ingots,0xFFFF,sunduk,False):
        MoveItem(FindItem(),20,Backpack(),0,0,0)

######### Mining

def mining():
    if TargetPresent():
        CancelTarget()
    print("Ушел руду копать.")
    with open('minoc_tiles.txt') as f:
        tiles = f.readlines()
        for t in tiles:
            NewMoveXY(t[0:4],t[5:9],True,1,True)
            UseType2(pickaxe)
            WaitTargetSelf()
            #print(f'Going to X:{t[13:17]} Y:{t[18:22]}')
            #print(f'Mine in X:{t[0:4]} Y:{t[5:9]} Z:{t[10:11]}')
            starttime = datetime.now()
            WaitJournalLineSystem(starttime, "You stop mining.|That is too far away.", 40000)
            ClearSystemJournal()
            amount_of_ore_in_backpack()
            drop_ore()
            fish_main()
            #pickaxe_main()
            """if FindTypeEx(0x0F2D,0x0ADC,Backpack(),0):
                goToChest()
                Wait(100)
                UseObject(sunduk)
                MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
            if FindTypeEx(0x0F2D,0x06FE,Backpack(),0):
                goToChest()
                Wait(100)
                UseObject(sunduk)
                MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
            if FindTypeEx(0x0F21,0x0B0E,Backpack(),0):
                goToChest()
                Wait(100)
                UseObject(sunduk)
                MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)"""
                
def drop_map():
    while FindType(map, Backpack()) > 5:
        Drop(FindItem(), 0, 0, 0, 0)
        Wait(100)
    AddToSystemJournal('Выбросил карты')

    
    
######### Dead Or Live
def ressurect():
    Wait(500)
    print("Walking to ressurect my self...")
    NewMoveXY(2545,630,True,1,True)
    print(PredictedX())
    print(PredictedY())
    if str(PredictedX()) == resX and str(PredictedY()) == resY:
        NewMoveXY(2545,631,True,1,True)
        Wait(500)
    else:
        main()
#########

def go_to_bank():
    NewMoveXY(2509,525,True,1,True)
    UOSay("Bank")
    Wait(500)
    
def cwd():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
    

def main():
    fish_main()
    #pickaxe_main()
    mining()
    ClearSystemJournal()
    amount_of_ore_in_bank()
            
if __name__ == '__main__':
    while True:
        main()