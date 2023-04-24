from datetime import datetime
from py_stealth import *

from staff import gold,runebook,horse,msg_crafter,msg_hunter,recall_Scrolls,market,home
from cheking import befor_hunt,medit
from dress import take_bow,take_kryss
from change_class import hunter
from load_unload_staff import load,unload
from brain import main_attack,main_loot


def hunting(file_location, gump_id, px, py):
    check_cast()
    Cast("polymorph")
    Wait(2000)
    befor_hunt()
    UseObject(runebook)
    WaitGump(gump_id)
    Wait(3000)

    while str(PredictedX()) != px and str(PredictedY()) != py:
        print(f"Current location: X={PredictedX()} Y={PredictedY()}")
        UseObject(runebook)
        WaitGump(gump_id)
        Wait(3000)
    else:
        with open(file_location) as f:
            tiles = f.readlines()
            for tile in tiles:
                NewMoveXY(tile[7:11], tile[12:16], True, 1, True)
                for i in range(2):
                    print(f"Check_cast, main_attack,loot,hunt {i}")
                    check_cast()
                    main_attack()
                    main_loot()
                    befor_hunt()

                current_x = str(PredictedX())
                current_y = str(PredictedY())
                print(f"PredictedX: {current_x}, PredictedY: {current_y}, FileName: {file_location}, GumpID: {gump_id}")

                with open("location/file_cast.txt", "w") as wf:
                    wf.write(f"{current_x}\n")
                    wf.write(f"{current_y}\n")
                    wf.write(f"{file_location}\n")
                    wf.write(f"{gump_id}\n")

                if GetStr(Self()) < 400:
                    check_cast()
                    print(file_location)
                    if str(file_location) == "location/despice.txt" or str(file_location) == "location/despice2lvl.txt":
                        pass
                    else:
                        hunting(file_location, gump_id, current_x, current_y)


def minoc_undead():
    UseObject(runebook)
    WaitGump(1034)
    Wait(5000)
    if str(PredictedX()) != "2468" and str(PredictedY()) != "1111":
        print(f"{PredictedX()} {PredictedY()}")
        minoc_undead()
    else:
        pass

def go_to_dungeon(name,x,y):
    Cast("polymorph")
    Wait(2000)
    befor_hunt()
    teleport(market,2130,804)
    SetWarMode(False)
    UseSkill("Hiding")
    Wait(10000)
    if Hidden():
        UseSkill("Stealth")
    Wait(1000)
    NewMoveXY(x,y,False,1,False)
    UOSay(name)
    Wait(2000)

def dungeon(say,fileLoc,x,y,dungX,dungY):
    go_to_dungeon(f"{say}", dungX, dungY)
    with open(f'{fileLoc}') as f:
        tile = f.readlines()
        for line in tile:
            NewMoveXY(line[7:11],line[12:16],True,1,True)
            main_attack()
            befor_hunt()
            main_attack()
            prex = PredictedX()
            prey = PredictedY()
            fillo = str(fileLoc)
            print(f'PredictedX: {str(PredictedX())}, PredictedY: {str(PredictedY())}, FileName: {fileLoc}')
            with open(f'location/file_cast.txt', 'w') as wf:
                wf.write(f"{prex}\n")
                wf.write(f"{prey}\n")
                wf.write(f"{fillo}\n")
            if GetStr(Self()) < 400:
                check_cast()
                (f"{fileLoc},{prex},{prey}")

def teleport(gump_id,x,y):
    UseObject(runebook)
    WaitGump(gump_id)
    Wait(3000)
    while PredictedX() != x and PredictedY() != y:
        print(f"{PredictedX()} {PredictedY()}")
        teleport(gump_id,x,y)

def charge_runebook():
    SetFindDistance(10)
    FindType(recall_Scrolls,Ground())
    print(f"взял с пола {str(CountEx(recall_Scrolls,0xFFFF,Ground()))} рекол скролов.")
    MoveXYZ(2846,175,26,True,1,True)
    Grab(FindItem(),FindFullQuantity())
    Wait(300)
    if FindType(recall_Scrolls,Backpack()):
        MoveItem(FindItem(),FindFullQuantity(),runebook,GetX(runebook),GetY(runebook),GetZ(runebook))
        startime = datetime.now()
        WaitJournalLineSystem(startime,"You put|runebook is fully charged.",1000)
    Wait(1500)
    while FindType(recall_Scrolls,Backpack()):
        DropHere(FindItem())
        Wait(500)

def hunt():
    start_time = datetime.now()
    UOSay(".showclasse")
    Wait(1000)
    
    if InJournalBetweenTimes(msg_hunter, start_time, datetime.now()) != -1:
        print("Class is Hunter.")
    elif InJournalBetweenTimes(msg_crafter, start_time, datetime.now()) != -1:
        print("Class is Crafter.")
        teleport(market,2130,804)
        hunter()
        
    locations = [
        ("location/spellbooks_0.txt", 1027, "1216", "660"),
        ("location/next_spellbook.txt", 1047, "3354", "293"),
        ("location/SB_1.txt", 1029, "3010", "694"),
        ("location/spellbook_2.txt", 1043, "2283", "1095"),
        ("location/SB_Minoc_Grave.txt", 1028, "2712", "796"),
        ("location/spellbook_minocM.txt", 1038, "2613", "82"),
        ("location/spellbooks_pook.txt", 1037, "2707", "1043"),
        ("location/spellbook_brit_0.txt", 1040, "1276", "1319"),
        ("location/spellbook_vozle_doma.txt", 1045, "2953", "471"),
        ("location/liches_0.txt", 1039, "2625", "1105"),
        ("location/ebooki.txt", 1046, "3225", "572")
    ]
    
    for location in locations:
        hunting(*location)

    dung_location = [   
    ("Despise","location/despice.txt", 5582, 631, 2128, 829),
    ("Despise","location/despice2lvl.txt", 5582, 631, 2128, 829),
    #("Hytloth","location/hytloth.txt", 5582, 631, 2128, 830),
    #("Wrong","location/wrong.txt", 5582, 631, 2128, 827)
    ]

    for location in dung_location:
        dungeon(*location)
      
def check_cast():
    if GetStr(Self()) < 400:
        teleport(home,2846,173)
        UOSay("cast me")
        MoveXYZ(2844, 172, 26, True, 1, True)
        unload()
        medit()
        load()
        charge_runebook()
        take_bow()
        Wait(1000)
        UOSay("Let's go to hunt some bustards!")
        