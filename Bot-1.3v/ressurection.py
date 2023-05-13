from py_stealth import *

def resurrect():
    print("resurrect")
    UOSay(".rescue")
    Wait(500)
    print("Walking to ressurect my self...")
    NewMoveXY(4248,2915,True,1,True)
    NewMoveXY(4248,2911,True,1,True)
    print(PredictedX())
    print(PredictedY())
    while Dead():
        NewMoveXY(4248,2915,True,1,True)
        NewMoveXY(4248,2911,True,1,True)