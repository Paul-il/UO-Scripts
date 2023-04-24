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
ore = 0x19B8
ingots = 0x1BF2
ore = 0x19B8
fish_20 = "20"
max_wight = 100
sunduk = 0x56E16687

######### Ore Colors
color = {'Iron':'0x0000','Copper':'0x0602','Black Dwarf':'0x0425','Pagan':'0x050C','Silver':'0x03E9','Spectral':'0x0483','Lavarock':'0x0486','Basilisk':'0x0487'}

######### Fish
def amount_fish_in_backpack():   # Work
    return(print(f'{str(CountEx(fish, 0xFFFF, Backpack()))} рыбы в паке.'))

def amount_fish_in_bank(): # Work
    return(print(f'{str(CountEx(fish, 0xFFFF, ObjAtLayer(BankLayer())))} рыбы в банке.'))
    
def move_fish_to_backpack_from_bank(): # Work
    if FindTypesArrayEx([fish], [0xFFFF], [ObjAtLayer(BankLayer())], True):
        FindTypesArrayEx([fish],[0xFFFF],[Backpack()],True)
        i = FindFullQuantity()
        Grab(FindTypesArrayEx([fish], [0xFFFF], [ObjAtLayer(BankLayer())], True), int(fish_20) - i)
        result = int(fish_20) - i
        print("взял с банка " + str(result) + " рыбы.")
        Wait(500)
        print("Теперь в паке " + str(count_fish_in_backpack()) + " рыбы.")
    else:
        print("В банке " + str(count_fish_in_bank()) + " рыбы.")
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
def make_pickaxe_from_chest():
    if FindTypeEx(ingots,0xFFFF,sunduk,False) > 20:
        print("начинаю делать кирки.")
        print(str(FindFullQuantity()) + " иногов в банке.")
        Grab(FindItem(),20)
        Wait(500)
        FindType(tinkering_tool,sunduk)
        Grab(FindItem(),1)
        Wait(500)
        UseType2(tinkering_tool)
        FindTypeEx([ingots],[0xFFFF],[Backpack()],False)
        WaitTargetObject(FindItem())
        Wait(500)
        WaitGump(400)
        Wait(500)
        WaitGump(3717)
        startime = datetime.now()
        WaitJournalLineSystem(startime,"You stop.",60000)
    else:
        print(str(FindFullQuantity()) + " кирок в банке.")
        MoveItem(FindItem(), 1,Backpack(), 0, 0, 0)
        Wait(100)
        check_pickaxe_in_the_backpack()
        
def move_pickaxe_to_the_backpack_from_chest():
    while FindTypesArrayEx([pickaxe], [0xFFFF], [sunduk], False):
        print("осталос " + str(FindFullQuantity()) + " кирок в банке.")
        MoveItem(FindTypeEx(pickaxe,0xFFFF,sunduk,False), 5, Backpack(),0,0,0)
        Wait(500)

def amount_pickaxe_in_chest():
    return(print(f'{str(CountEx(pickaxe, 0xFFFF, sunduk))} кирок в банке.'))

def check_pickaxe_in_backpack():
    return(print(f'{str(CountEx(pickaxe, 0xFFFF, Backpack()))} кирок в паке.'))
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
def amount_of_ore_in_chest(): # Work
    return (print(f"Iron: {CountEx(ore,0x0000,sunduk)},Copper: {CountEx(ore,0x0602,sunduk)},Black Dwarf: {CountEx(ore,0x0425,sunduk)},Pagan: {CountEx(ore,0x050C,sunduk)},Silver: {CountEx(ore,0x03E9,Bsunduk)},Spectral: {CountEx(ore,0x0483,sunduk)}, Lavarock: {CountEx(ore,0x0486,sunduk)}, Icerock: {CountEx(ore,0x04E7,sunduk)}, Mythril: {CountEx(ore,0x0492,sunduk)},Basilisk: {CountEx(ore,0x0487,sunduk)},Sun: {CountEx(ore,0x0514,sunduk)},Deadra: {CountEx(ore,0x0494,sunduk)},Doom: {CountEx(ore,0x049F,sunduk)},New Zulu: {CountEx(ore,0x0488,sunduk)},Paradise Gem: {CountEx(ore,0x06FE,sunduk)},Hell Gem: {CountEx(ore,0x0ADC,sunduk)},Void Gem: {CountEx(ore,0x0B0E,sunduk)}."))

def amount_of_ore_in_backpack(): # Work
    return (print(f"Iron: {CountEx(ore,0x0000,Backpack())},Copper: {CountEx(ore,0x0602,Backpack())},Black Dwarf: {CountEx(ore,0x0425,Backpack())},Pagan: {CountEx(ore,0x050C,Backpack())},Silver: {CountEx(ore,0x03E9,Backpack())},Spectral: {CountEx(ore,0x0483,Backpack())}, Lavarock: {CountEx(ore,0x0486,Backpack())}, Icerock: {CountEx(ore,0x04E7,Backpack())}, Mythril: {CountEx(ore,0x0492,Backpack())},Basilisk: {CountEx(ore,0x0487,Backpack())},Sun: {CountEx(ore,0x0514,Backpack())},Deadra: {CountEx(ore,0x0494,Backpack())},Doom: {CountEx(ore,0x049F,Backpack())},New Zulu: {CountEx(ore,0x0488,Backpack())},Paradise Gem: {CountEx(ore,0x06FE,Backpack())},Hell Gem: {CountEx(ore,0x0ADC,Backpack())},Void Gem: {CountEx(ore,0x0B0E,Backpack())}."))  

def move_ore_to_chest_from_backpack():  # Work
    while FindTypeEx(ore,0xFFFF,Backpack,False):
        MoveItem(FindItem(),FindFullQuantity(),Backpack(),0,0,0)
        
######### Chest

def goToChest():  # Work
    NewMoveXY(1056,1304,True,1,True)
    
def move_ingots_to_backpack_from_chest():  # Work
    if FindTypeEx(ingots,0xFFFF,sunduk,False):
        MoveItem(FindItem(),20,Backpack(),0,0,0)

def move_ingots_to_backpack_from_chest():  # Work
    if FindTypeEx(ingots,0xFFFF,sunduk,False):
        MoveItem(FindItem(),8,Backpack(),0,0,0)

######### Mining

def mining():
    with open('tiles.txt') as f:
        tiles = f.readlines()
        for t in tiles:
            if TargetPresent():
                CancelTarget()
            NewMoveXY(t[13:17],t[18:22],True,1,True)
            UseType2(pickaxe)
            WaitTargetXYZ(t[0:4],t[5:9],t[10:11])
            #print(t[0:4],t[5:9],t[10:11])
            #print(t[13:17],t[18:22])
            starttime = datetime.now()
            WaitJournalLineSystem(starttime, "You stop mining.|That is too far away.", 30000)
                

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


def go_to_bank():
    NewMoveXY(2509,525,True,1,True)
    UOSay("Bank")
    Wait(500)
    
def cwd():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
    

def main():
    if str(check_pickaxe_in_backpack()) > str(2):
        pass
    else:
        goToChest()
        UseType(sunduk)
        make_pickaxe_from_chest()

if __name__ == '__main__':
    if True:
        amount_of_ore_in_backpack()