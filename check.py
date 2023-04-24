from py_stealth import *
from datetime import *
import timeit
from itertools import chain
from staff import *

warrior_name = ["Ogre","Ettin","Frankenstein","Skeletal","Mummy","Revenant","Carcass","Dracula","Troll"]
mage_name = ["book","marksman","archer","Liche","Daemon","Fiend","wisp","Drake","Dragon","hunter"]

run = ["behemoth","wyrm","gold"]
player_names = ["Korvin","Milda","Mag","Nebuchadnezzar","Legolas","Lord Vader","Kolobok","Athena","Proleska","Eva"]
name = [0x0027,0x00CA,0x03D9,0x0001,0x0003,0x0035,0x0036,0x0037,0x0038,0x0039,0x003C,0x003A,0x003B,0x0018,0x023E,0x000C,0x0009]
bow = 0x66F3

human = 0x0190


def find_npc1():
    found = []
    SetFindDistance(20)
    for npc in name:
        FindType(npc, Ground())
        found += GetFindedList()
    return found


def task_a():
    #print(f"Length of NPC': {len(find_npc())}")
    for npc in find_npc():
        for i in mage_name:
            if i in str(GetName(npc)):
                print(f"Distance: {str(GetDistance(npc))} Name: {str(GetName(npc))} Length of NPC's: {len(find_npc())}")
                if str(GetDistance(npc)) < "3":
                    NewMoveXY(GetX(npc)+4,GetY(npc)-4,True,1,True)
        for i in warrior_name:
            if i in str(GetName(npc)):
                print(f"Name: {str(GetName(npc))} Length of NPC's: {len(find_npc())}")
                if str(GetDistance(npc)) < "2":
                    pass
        for i in run:
            if i in str(GetName(npc)):
                if str(GetDistance(npc)) < "10":
                    NewMoveXY(GetX(npc),GetY(npc),Ture,1,True)

            
def task_b():
    if not Dead():
        if GetMaxHP(Self()) < 550:
            print(f"HP: {str(GetHP(Self()))} Name: {GetName(Self())}")
            Wait(100)
        
def hello(msg):
    pass
def run_parallel(*functions):
    '''
    Run functions in parallel
    '''
    from multiprocessing import Process
    processes = []
    for function in functions:
        proc = Process(target=function)
        proc.start()
        processes.append(proc)
    for proc in processes:
        proc.join()
       
def main():
    run_parallel(task_a(),task_b(),hello(msg="konstantinos"))

    
def testing():
    found = []
    UseObject(sunduk)
    for i in loot:
        FindType(i,sunduk)
        print(f"{str(GetAltName(FindItem()))}")
        #print(f"{GetClilocByID(1042971)}")
        found += GetFindedList()
        
    print(f"{len(found)} Item's in sunduk")
    

def find_npc():
    found = []
    SetFindDistance(10)
    for npc in [0x0001,0x0003,0x0009,0x0027,0x0035,0x0036,0x0037,0x0038,0x0039,0x00CA,0x03D9,0x003C,0x003A,0x003B,0x0018,0x023E,0x000C]:
        FindType(npc, Ground())
        found += GetFindedList()
    return found

def main_attack():
    for npc in find_npc():
        ClientPrint(f"Вокруг меня {len(find_npc())} монстра.")
        try:
            print(f"Номер монстра: {find_npc().index(npc)}.")
        except:
            pass
        while len(find_npc()) >= 1:
            CastToObject("chain lightning",npc)
            #Wait(1900)
            medit()
            for i in warrior_name:
                if i in str(GetName(npc)):
                    SetWarMode(True)
                    print(str(GetName(npc)))
                    print(f'До {str(GetName(npc))} {str(GetDistance(npc))} шагов.')
                    while GetHP(npc) > 0:
                        Attack(npc)
                        NewMoveXY(GetX(Self())-4,GetY(Self())-4,True,1,True)
                        #tamla()
                        medit()
                        while Paralyzed():
                            NewMoveXY(GetX(Self())-4,GetY(Self())-4,True,1,True)
                            NewMoveXY(GetX(Self())+6,GetY(Self())-6,True,1,True)
                            NewMoveXY(GetX(npc),GetY(npc),True,1,True)
                            #tamla()
                            medit()

            for i in mage_name:
                if i in str(GetName(npc)):
                    NewMoveXY(GetX(npc)-4,GetY(npc)-4,True,1,True)
                    SetWarMode(True)
                    while GetHP(npc) > 0:
                        Attack(npc)
                        CastToObject("chain lightning",npc)
                        NewMoveXY(GetX(npc)-4,GetY(npc)-4,True,1,True)
                        #tamla()
                        Wait(2000)
                        medit()
                        while Paralyzed():
                            NewMoveXY(GetX(Self())-4,GetY(Self())-4,True,1,True)
                            NewMoveXY(GetX(Self())+6,GetY(Self())-6,True,1,True)
                            #tamla()
                            medit()

            if "Undead" in str(GetName(npc)) or "Dracoliche" in str(GetName(npc)):
                take_bow()
                SetWarMode(True)
                while GetHP(npc) > 0:
                    Attack(npc)
                    CastToObject("resurrection",npc)
                    NewMoveXY(GetX(npc)-4,GetY(npc)+4,True,1,True)
                    #tamla()
                    Wait(2200)
                    medit()
                    while Paralyzed():
                        NewMoveXY(GetX(Self())-4,GetY(Self())-4,True,1,True)
                        NewMoveXY(GetX(Self())+6,GetY(Self())-6,True,1,True)
                        #tamla()
                        medit()

            Ignore(npc)    
    find_npc()
    medit()

def medit():
    if GetMana(Self()) < 200:
        SetWarMode(False)
        UseSkill("Meditation")
        startime = datetime.now()
        WaitJournalLineSystem(startime,"You stop meditating.|You moved and lost your concetration.",5000)


def buy_horse():
    SetAutoBuyDelay(1000)
    print("buy_horse")
    SetFindDistance(5)
    FindType(gold,hunt_pack)
    if FindFullQuantity() >= 320:
        UseObject(runebook)
        WaitGump(1042)
        Wait(5000)
        if str(PredictedX()) != "4438" and str(PredictedY()) != "1179":
            print(f"{PredictedX()} {PredictedY()}")
            buy_horse()
        UOSay("buy")

        CheckLag(1000)
        AutoBuy(0x2120,0xFFFF,1)
        CheckLag(1000)
        NewMoveXY(GetX(FindItem()),GetY(FindItem()),True,1,True)
        FindType(horse,Ground())
        UseObject(FindItem())
    else:
        if FindTypeEx(gold,0x0000,ObjAtLayer(BankLayer())):
            MoveItem(FindItem(),320,Backpack(),0,0,0)
            Wait(1000)
        FindType(gold,Backpack())
        if FindFullQuantity() >= 320:
            UseObject(runebook)
            WaitGump(1042)
            Wait(5000)
            if str(PredictedX()) != "4438" and str(PredictedY()) != "1179":
                print(f"{PredictedX()} {PredictedY()}")
                buy_horse()

            UOSay("buy")

            CheckLag(1000)
            GetShopList()
            AutoBuy(0x2120,0x0000,1)
            CheckLag(1000)
            FindType(horse,Ground())
            NewMoveXY(GetX(FindItem()),GetY(FindItem()),True,1,True)
            UseObject(FindItem())
        else:
            print("buy_horse: Somthing Goes Wrong!")
            

def abc():
    for i in range(7):
        print(i+1)
    

            
        

    
if __name__ == '__main__':
    if True:
        buy_horse()

