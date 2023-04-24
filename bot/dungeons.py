import from recalls *

def go_to_wrong():
    #recall_to_Market()
    SetFindDistance(10)
    NewMoveXY(2128,828,True,1,True)
    UOSay("Wrong")

def go_to_despice():
    check_befor_hunt()
    recall_to_Market()
    NewMoveXY(2128,829,True,1,True)
    UOSay("Despise")
    Wait(2000)
    Cast("polymorph")
    with open('despice.txt') as f:
        tile = f.readlines()
        for line in tile:
            NewMoveXY(line[7:11],line[12:16],True,1,True)
            main_attack()
            check_befor_hunt()

def go_to_hytloth():
    NewMoveXY(2132,829,True,1,True)
    UOSay("hytloth")
    Wait(2000)
