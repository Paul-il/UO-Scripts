from datetime import datetime
from py_stealth import *

from staff import gold,runebook,horse,recall_Scrolls,msg_crafter,msg_hunter
from cheking import befor_hunt
from dress import take_bow,take_kryss
from change_class import hunter
from load_unload_staff import load,unload
from brain import main_attack

def hunting(fileLoc,gumpID,px,py):
    check_cast()
    Cast("polymorph")
    Wait(2000)
    befor_hunt()
    UseObject(runebook)
    WaitGump(gumpID)
    Wait(3000)
    while str(PredictedX()) != px and str(PredictedY()) != py:
        print(f"{PredictedX()} {PredictedY()}")
        UseObject(runebook)
        WaitGump(gumpID)
        Wait(3000)
    else:
        with open(f'{fileLoc}') as f:
            tile = f.readlines()
            for line in tile:
                NewMoveXY(line[7:11],line[12:16],True,1,True)
                check_cast()
                main_attack()
                befor_hunt()
                main_attack()
                check_cast()
                locations = [str(PredictedX()), str(PredictedY()), f'{fileLoc}, {gumpID}']
                prex = str(PredictedX())
                prey = str(PredictedY())
                fillo = str(fileLoc)
                gump = str(gumpID)
                print(f'PredictedX: {str(PredictedX())}, PredictedY: {str(PredictedY())}, FileName: {fileLoc}, GumpID: {gumpID}')
                with open(f'location/file_cast.txt', 'w') as wf:
                    wf.write(f"{prex}\n")
                    wf.write(f"{prey}\n")
                    wf.write(f"{fillo}\n")
                    wf.write(f"{gump}\n")
                    if GetStr(Self()) < 390:
                        check_cast()
                        hunting(fillo,gump,prex,prey)
                    else: pass
        
def minoc_undead():
    UseObject(runebook)
    WaitGump(1034)
    Wait(5000)
    if str(PredictedX()) != "2468" and str(PredictedY()) != "1111":
        print(f"{PredictedX()} {PredictedY()}")
        minoc_undead()
    else:
        pass
        
def despice(fileLoc,x,y):
    if GetStr(Self()) < 390:
        check_cast()
        despice("location/despice2lvl.txt")
    else: pass
    Cast("polymorph")
    Wait(2000)
    befor_hunt()
    market()
    SetWarMode(False)
    UseSkill("Hiding")
    Wait(10000)
    if Hidden():
        UseSkill("Stealth")
    Wait(1000)
    NewMoveXY(2128,829,False,1,False)
    UOSay("Despise")
    Wait(1000)
    with open(f'{fileLoc}') as f:
        tile = f.readlines()
        for line in tile:
            NewMoveXY(line[7:11],line[12:16],True,1,True)
            main_attack()
            befor_hunt()
            main_attack()
            prex = str(PredictedX())
            prey = str(PredictedY())
            fillo = str(fileLoc)
            print(f'PredictedX: {str(PredictedX())}, PredictedY: {str(PredictedY())}, FileName: {fileLoc}')
            with open(f'location/file_cast.txt', 'w') as wf:
                wf.write(f"{prex}\n")
                wf.write(f"{prey}\n")
                wf.write(f"{fillo}\n")
            if GetStr(Self()) < 390:
                check_cast()
                despice("location/despice.txt",prex,prey)
            else: pass

def despice2lvl(fileLoc,x,y):
    if GetStr(Self()) < 390:
        check_cast()
        despice("location/despice2lvl.txt")
    else: pass
    Cast("polymorph")
    Wait(2000)
    befor_hunt()
    market()
    SetWarMode(False)
    UseSkill("Hiding")
    Wait(10000)
    if Hidden():
        UseSkill("Stealth")
    Wait(1000)
    NewMoveXY(2128,829,False,1,False)
    UOSay("Despise")
    Wait(1000)
    with open(f'{fileLoc}') as f:
        tile = f.readlines()
        for line in tile:
            NewMoveXY(line[7:11],line[12:16],True,1,True)
            main_attack()
            befor_hunt()
            main_attack()
            prex = str(PredictedX())
            prey = str(PredictedY())
            fillo = str(fileLoc)
            print(f'PredictedX: {str(PredictedX())}, PredictedY: {str(PredictedY())}, FileName: {fileLoc}')
            with open(f'location/file_cast.txt', 'w') as wf:
                wf.write(f"{prex}\n")
                wf.write(f"{prey}\n")
                wf.write(f"{fillo}\n")
                if GetStr(Self()) < 390:
                    check_cast()
                    despice("location/despice2lvl.txt",prex,prey)
                else: pass
            
def market():
    print("recall_to_Market")
    UseObject(runebook)
    WaitGump(1025)
    Wait(3000)
    while str(PredictedX()) != "2130" and str(PredictedY()) != "804":
        print(f"{PredictedX()} {PredictedY()}")
        market()

def home():
    UseObject(runebook)
    WaitGump(1031)
    Wait(3000)
    while str(PredictedX()) != "2846" and str(PredictedY()) != "173":
        print(f"{PredictedX()} {PredictedY()}")
        home()

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
    start = datetime.now()
    UOSay(".showclasse")
    Wait(1000)
    if InJournalBetweenTimes(msg_hunter, start, datetime.now()) != -1:
        print("Class is Hunter.")
    
    elif InJournalBetweenTimes(msg_crafter, start, datetime.now()) != -1:
        print("Class is Crafter.")
        market()
        hunter()

    locations = [
        #("location/spellbooks_0.txt",1027,"1216","660"),
        ("location/next_spellbook.txt",1047,"3354","293"),
        ("location/SB_1.txt",1029,"3010","694"),
        ("location/spellbook_2.txt",1043,"2283","1095"),
        ("location/SB_Minoc_Grave.txt",1028,"2712","796"),
        ("location/spellbook_minocM.txt",1038,"2613","82"),
        ("location/spellbooks_pook.txt",1037,"2707","1043"),
        ("location/spellbook_brit_0.txt",1040,"1276","1319"),
        ("location/spellbook_vozle_doma.txt",1045,"2953","471"),
        #("location/ebooki.txt",1046,"3225","572"),
    ]
    
    for location in locations:
        hunting(*location)

    despice("location/despice.txt","5582","631")
    despice2lvl("location/despice2lvl.txt","5582","631")


def hunt_event():
    start = datetime.now()
    UOSay(".showclasse")
    Wait(1000)
    if InJournalBetweenTimes(msg_hunter, start, datetime.now()) != -1:
        print("Class is Hunter.")
    
    elif InJournalBetweenTimes(msg_crafter, start, datetime.now()) != -1:
        print("Class is Crafter.")
        market()
        hunter()

    spellbook("location/spellbooks_0.txt",1027,"1216","660")
    spellbook("location/next_spellbook.txt",1047,"3354","293")
    spellbook("location/SB_1.txt",1029,"3010","694")
    spellbook("location/spellbook_2.txt",1043,"2283","1095")
    spellbook("location/SB_Minoc_Grave.txt",1028,"2712","796")
    spellbook("location/spellbook_minocM.txt",1038,"2613","82")
    spellbook("location/spellbooks_pook.txt",1037,"2707","1043")
    spellbook("location/spellbook_brit_0.txt",1040,"1276","1319")
    spellbook_vozle_doma()
      

def check_cast():
    if GetStr(Self()) < 390:
        UseObject(runebook)
        WaitGump(1031)
        Wait(5000)
        while str(PredictedX()) != "2846" and str(PredictedY()) != "173":
            print(f"{PredictedX()} {PredictedY()}")
            UseObject(runebook)
            WaitGump(1031)
            Wait(5000)
        UOSay("cast me")
        MoveXYZ(2844,172,26,True,1,True)
        unload()
        SetWarMode(False)
        UseSkill("Meditation")
        load()
        FindType(recall_Scrolls,Ground())
        print(f"{str(CountEx(recall_Scrolls,0xFFFF,Ground()))} Recalls left.")
        MoveXYZ(2846,175,26,True,1,True)
        Grab(FindItem(),FindFullQuantity())
        Wait(300)
        if FindType(recall_Scrolls,Backpack()):
            MoveItem(FindItem(),FindFullQuantity(),runebook,GetX(runebook),GetY(runebook),GetZ(runebook))
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You put|runebook is fully charged.",1000)
        Wait(500)
        while FindType(recall_Scrolls,Backpack()):
            DropHere(FindItem())
            Wait(200)
        take_bow()
        Wait(1000)
        UOSay("Let's Go to Hunt Some Bustards!")
           
                