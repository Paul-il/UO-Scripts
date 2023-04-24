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
        goToChest()
        UseObject(sunduk)
        move_fish_to_backpack_from_chest()
    else:
        pass

def amount_fish_in_backpack():   # Work
    return(CountEx(fish, 0xFFFF, Backpack()))

def amount_fish_in_chest(): # Work
    return(print(f'{str(CountEx(fish, 0xFFFF, sunduk))} рыбы в банке.'))
    
def move_fish_to_backpack_from_chest(): # Work
    if FindType(fish, sunduk):
        FindType(fish,Backpack())
        i = FindFullQuantity()
        if i >= 20:
            pass
        else:
            Grab(FindType(fish, sunduk), int(fish_20) - i)
            result = int(fish_20) - i
            print(f'взял с сундука {result}  рыбы.')
            Wait(500)
            CheckLag(100)
            print(f'Теперь в паке {str(CountEx(fish, 0xFFFF, Backpack()))} рыбы.')
    else:
        print(f'в сундуке осталось {str(CountEx(fish, 0xFFFF, sunduk))} рыбы.')
        Wait(500)
        CheckLag(100)
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
            CheckLag(100)
            UseType2(tinkering_tool)
            WaitTargetObject(FindItem())
            Wait(500)
            CheckLag(100)
            WaitGump(100)
            Wait(500)
            CheckLag(100)
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
    if str(amount_pickaxe_in_backpack()) < str(2):
        goToChest()
        Wait(500)
        CheckLag(100)
        UseObject(sunduk)
        Wait(500)
        CheckLag(100)
        if amount_pickaxe_in_chest():
            while str(amount_pickaxe_in_backpack()) < str(5):
                move_pickaxe_to_the_backpack_from_chest()
                UseObject(sunduk)
                Wait(500)
                CheckLag(100)
                print(f'{str(amount_pickaxe_in_chest())} кирок в сундуке')
                print(f'{str(amount_pickaxe_in_backpack())} кирок в паке')
        else:
            make_pickaxe_from_chest()
            move_pickaxe_to_the_chest_from_backpack()

def make_pickaxe_from_chest():
    if FindTypeEx(ingots,0x0486,sunduk,False) > 20:
        print("начинаю делать кирки.")
        print(str(FindFullQuantity()) + " иногов в сундуке.")
        Grab(FindItem(),20)
        Wait(500)
        CheckLag(100)
        if FindType(tinkering_tool,Backpack()):
            UseType2(tinkering_tool)
            FindTypeEx(ingots,0x0486,Backpack(),False)
            WaitTargetObject(FindItem())
            Wait(500)
            CheckLag(100)
            WaitGump(400)
            Wait(500)
            CheckLag(100)
            WaitGump(3717)
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You stop.",5000)
        else:
            FindType(tinkering_tool,sunduk)
            Grab(FindItem(),1)
            Wait(500)
            CheckLag(100)
            if FindType(tinkering_tool,Backpack()):
                UseType2(tinkering_tool)
                FindTypeEx(ingots,0x0486,Backpack(),False)
                WaitTargetObject(FindItem())
                Wait(500)
                CheckLag(100)
                WaitGump(400)
                Wait(500)
                CheckLag(100)
                WaitGump(3717)
                startime = datetime.now()
                WaitJournalLineSystem(startime,"You stop.",15000)
            else:
                make_pickaxe_from_chest()
    else:
        print(str(FindFullQuantity()) + " кирок в сундуке.")
        MoveItem(FindItem(), 1,Backpack(), 0, 0, 0)
        Wait(100)
        CheckLag(100)
        print(f'{amount_pickaxe_in_backpack()} кирок в сумке')
        
def move_pickaxe_to_the_backpack_from_chest():
    if FindType(pickaxe, sunduk):
        Wait(500)
        CheckLag(100)
        ClearSystemJournal()
        print("осталос " + str(FindFullQuantity()) + " кирок в сундуке.")
        FindType(pickaxe, Backpack())
        while FindFullQuantity() < 5:
            FindType(pickaxe, sunduk)
            MoveItem(FindItem(), 1, Backpack(),0,0,0)
            Wait(500)
            CheckLag(100)

def move_pickaxe_to_the_chest_from_backpack():
    if FindType(pickaxe, Backpack()):
        print("осталос " + str(FindFullQuantity()) + " кирок в паке.")
        MoveItem(FindType(pickaxe,Backpack()), 1, sunduk,0,0,0)
        Wait(500)
        CheckLag(100)

def amount_pickaxe_in_chest():
    UseObject(sunduk)
    Wait(500)
    return(str(CountEx(pickaxe, 0xFFFF, sunduk)))

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
def amount_of_ore_in_chest(): # Work
    return (print(f"Iron: {CountEx(ore,0x0000,sunduk)},Copper: {CountEx(ore,0x0602,sunduk)},Black Dwarf: {CountEx(ore,0x0425,sunduk)},Pagan: {CountEx(ore,0x050C,sunduk)},Silver: {CountEx(ore,0x03E9,Bsunduk)},Spectral: {CountEx(ore,0x0483,sunduk)}, Lavarock: {CountEx(ore,0x0486,sunduk)}, Icerock: {CountEx(ore,0x04E7,sunduk)}, Mythril: {CountEx(ore,0x0492,sunduk)},Basilisk: {CountEx(ore,0x0487,sunduk)},Sun: {CountEx(ore,0x0514,sunduk)},Deadra: {CountEx(ore,0x0494,sunduk)},Doom: {CountEx(ore,0x049F,sunduk)},New Zulu: {CountEx(ore,0x0488,sunduk)},Paradise Gem: {CountEx(ore,0x06FE,sunduk)},Hell Gem: {CountEx(ore,0x0ADC,sunduk)},Void Gem: {CountEx(ore,0x0B0E,sunduk)}."))

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
        for i in colors:
            FindTypeEx(ore,i,Backpack())
            Drop(FindItem(), 0, 0, 0, 0)
            Wait(100)
            CheckLag(100)
        goToChest()
        UseObject(sunduk)
        move_ore_to_chest_from_backpack()

######### Chest

def goToChest():  # Work
    NewMoveXY(1513,2760,True,1,True)
   
def goToCave():
    NewMoveXY(1499,2830,True,1,True)
    
def move_ingots_to_backpack_from_chest():  # Work
    if FindTypeEx(ingots,0xFFFF,sunduk,False):
        MoveItem(FindItem(),20,Backpack(),0,0,0)

######### Mining

def mining():
    if TargetPresent():
        CancelTarget()
    print("Ушел руду копать.")
    with open('location/trinsic_tiles.txt') as f:
        tiles = f.readlines()
        for t in tiles:
            pickaxe_main()
            fish_main()
            drop_ore()
            #NewMoveXY(t[13:17],t[18:22],True,1,True)
            NewMoveXY(t[7:11],t[12:16],True,1,True)
            UseType2(pickaxe)
            WaitTargetSelf()
            #WaitTargetXYZ(t[0:4],t[5:9],t[10:11])
            #print(f'Going to X:{t[13:17]} Y:{t[18:22]}')
            #print(f'Mine in X:{t[0:4]} Y:{t[5:9]} Z:{t[10:11]}')
            starttime = datetime.now()
            WaitJournalLineSystem(starttime, "You stop mining.|That is too far away.", 60000)
            if FindTypeEx(0x0F2D,0x0ADC,Backpack(),0):
                goToChest()
                Wait(100)
                CheckLag(100)
                UseObject(sunduk)
                MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
            if FindTypeEx(0x0F2D,0x06FE,Backpack(),0):
                goToChest()
                Wait(100)
                CheckLag(100)
                UseObject(sunduk)
                MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
            if FindTypeEx(0x0F21,0x0B0E,Backpack(),0):
                goToChest()
                Wait(100)
                CheckLag(100)
                UseObject(sunduk)
                MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
                
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
    

def mining_main():
    pickaxe_main()
    fish_main()
    mining()
    goToCave()
    ClearSystemJournal()
            
            

            
if __name__ == '__main__':
    while True:
        mining_main()