from staff import sunduk,hunt_pack,arrows,ice_color,fish,bottle,tamla_color,bandages
from datetime import datetime
from py_stealth import *

def unload():
    MoveXYZ(2849,173,26,True,1,True)
    UseObject(sunduk)
    EmptyContainer(hunt_pack,sunduk,500)

####### Load

def load():
    regi = [BP(),BM(),GA(),GS(),MR(),NS(),SA(),SS()]
    thousand = 1000
    hundred = 100
    MoveXYZ(2849,173,26,True,1,True)
    UseObject(sunduk)
    #FindType(arrows,Backpack())
    #MoveItem(FindItem(),FindFullQuantity(),sunduk,0,0,0)
    FindTypeEx(arrows,ice_color,Backpack(),False)
    if FindFullQuantity() < thousand:
        print(f"Amount of Fire Arrows in Backpack: {FindFullQuantity()}.")
        result = thousand - FindFullQuantity()
        FindTypeEx(arrows,ice_color,sunduk,False)
        MoveItem(FindItem(),result,hunt_pack,0,0,0)
        Wait(500)
        
    FindType(bandages,Backpack())
    if FindFullQuantity() < thousand:
        print(FindFullQuantity())
        result = thousand - FindFullQuantity()
        FindType(bandages,sunduk)
        MoveItem(FindItem(),result,hunt_pack,0,0,0)
        Wait(500)
    for i in regi:
        FindType(i,Backpack())
        if FindFullQuantity() < hundred:
            result = hundred - FindFullQuantity()
            FindType(i,sunduk)
            MoveItem(FindItem(),result,hunt_pack,0,0,0)
            Wait(500)
    FindType(fish,Backpack())
    if FindFullQuantity() < 20:
        result = 20 - FindFullQuantity()
        FindType(fish,sunduk)
        MoveItem(FindItem(),result,Backpack(),0,0,0)
        Wait(500)
    FindTypeEx(bottle,tamla_color,sunduk,False)
    if FindFullQuantity() > 10:
        FindTypeEx(bottle,tamla_color,hunt_pack,False)
        result = 10 - FindFullQuantity()
        FindTypeEx(bottle,tamla_color,sunduk,False)
        MoveItem(FindItem(),result,hunt_pack,0,0,0)
          