from staff import box,hammer,stormteal_color,logs,bow
from py_stealth import *
    
def repair_bow():
    Disarm()
    MoveXYZ(2852,176,26,True,1,True)
    if TargetPresent():
        CancelTarget()
    UseObject(box)
    Wait(200)
    FindType(hammer,box)
    Wait(200)
    MoveItem(FindItem(),1,Backpack(),0,0,0)
    Wait(500)
    UseType2(hammer)
    FindTypeEx(logs,stormteal_color,box,False)
    MoveItem(FindItem(),100,Backpack(),0,0,0)
    Wait(500)
    #MoveXYZ(2852,176,26,True,1,True)
    UseType2(hammer)
    FindType(bow,Backpack())
    WaitTargetObject(FindItem())
    WaitGump(161)
    Wait(3000)
    #MoveXYZ(2849,174,26,True,1,True)
    Disarm()
    Wait(500)
    UseObject(box)
    FindType(hammer,Backpack())
    MoveItem(FindItem(),1,box,0,0,0)
    Wait(500)
    FindType(logs,Backpack())
    MoveItem(FindItem(),FindFullQuantity(),box,0,0,0)
    Wait(500)
    