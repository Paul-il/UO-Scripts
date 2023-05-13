from staff import gold,hunt_pack,horse,runebook

def checking_place():
    print("Checking Place")
    if str(PredictedX()) != "4438" and str(PredictedY()) != "1179":
        print("Wrong Place")
        print(f"{PredictedX()} {PredictedY()}")
        buy_horse()
    else:
        print("Correct place")

def buying():
    print("Going To Buy a Horse")
    UseObject(runebook)
    WaitGump(1041)
    Wait(5000)
    checking_place()
    UOSay("buy")
    Wait(1000)
    AutoBuy(0x2120,0xFFFF,1)
    Wait(1000)
    FindType(horse,Ground())
    NewMoveXY(GetX(FindItem()),GetY(FindItem()),True,1,True)
    UseObject(FindItem())
    print("Im on a Horse")

def buy_horse():
    UOSay("Bank")
    print("Start buy horse function")
    SetFindDistance(5)
    if not FindType(gold,hunt_pack):
        FindTypeEx(gold,0xFFFF,ObjAtLayer(BankLayer()))
        MoveItem(FindItem(),320,Backpack(),0,0,0)
        Wait(1000)
        if FindType(gold,Backpack()) >= 320:
            buying()
    else:
        buying()
