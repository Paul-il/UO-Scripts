from recall import teleport
from staff import SelfSTR,market
from brain import main_attack
from cheking_cast import check_cast
from befor_hunting import befor_hunt

from py_stealth import *

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
            prex = PredictedX()
            prey = PredictedY()
            fillo = str(fileLoc)
            print(f'PredictedX: {str(PredictedX())}, PredictedY: {str(PredictedY())}, FileName: {fileLoc}')
            with open(f'location/file_cast.txt', 'w') as wf:
                wf.write(f"{prex}\n")
                wf.write(f"{prey}\n")
                wf.write(f"{fillo}\n")
            if GetStr(Self()) < SelfSTR:
                check_cast()
                (f"{fileLoc},{prex},{prey}")