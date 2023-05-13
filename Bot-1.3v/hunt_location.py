from staff import runebook,market,msg_crafter,msg_hunter,SelfSTR

from brain import main_attack,main_loot
from befor_hunting import befor_hunt
from cheking_cast import check_cast
from change_class import hunter
from dungoen import dungeon
from recall import teleport

from datetime import datetime
from py_stealth import *

def hunting(file_location, gump_id, px, py):
    check_cast()
    Cast("polymorph")
    Wait(2000)
    befor_hunt()
    UseObject(runebook)
    WaitGump(gump_id)
    Wait(3000)

    if str(PredictedX()) != px and str(PredictedY()) != py:
        print(f"Current location: X={PredictedX()} Y={PredictedY()}")
        UseObject(runebook)
        WaitGump(gump_id)
        Wait(3000)
    else:
        with open(file_location) as f:
            tiles = f.readlines()
            for tile in tiles:
                NewMoveXY(tile[7:11], tile[12:16], True, 1, True)
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

                if GetStr(Self()) < SelfSTR:
                    check_cast()
                    print(file_location)
                    if str(file_location) == "location/despice.txt" or str(file_location) == "location/despice2lvl.txt":
                        pass
                    else:
                        hunting(file_location, gump_id, current_x, current_y)

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
        ("location/next_spellbook.txt", 1046, "3354", "293"),
        ("location/SB_1.txt", 1029, "3010", "694"),
        ("location/spellbook_2.txt", 1042, "2283", "1095"),
        ("location/SB_Minoc_Grave.txt", 1028, "2712", "796"),
        ("location/spellbook_minocM.txt", 1037, "2613", "82"),
        ("location/spellbooks_pook.txt", 1036, "2707", "1043"),
        ("location/spellbooks_0.txt", 1027, "1216", "660"),
        ("location/spellbook_brit_0.txt", 1039, "1276", "1319"),
        ("location/spellbook_vozle_doma.txt", 1044, "2953", "471"),
        ("location/liches_0.txt", 1038, "2625", "1105"),
        ("location/ebooki.txt", 1045, "3225", "572")
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