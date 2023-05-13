from staff import home,SelfSTR
from bow import take_bow
from recall import teleport
from load_unload import unload,load
from runebook import charge_runebook

def check_cast():
    if GetStr(Self()) < SelfSTR:
        teleport(home,2846,173)
        UOSay("cast me")
        MoveXYZ(2844, 172, 26, True, 1, True)
        unload()
        SetWarMode(False)
        UseSkill("Meditation")
        load()
        charge_runebook()
        take_bow()
        Wait(1000)
        UOSay("Let's go to hunt some bustards!")