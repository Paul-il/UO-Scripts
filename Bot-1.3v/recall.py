from staff import (runebook,home,market
                   )

from py_stealth import *

def teleport(gump_id,x,y):
    UseObject(runebook)
    WaitGump(gump_id)
    Wait(3000)
    while PredictedX() != x and PredictedY() != y:
        print(f"{PredictedX()} {PredictedY()}")
        teleport(gump_id,x,y)

def go_home():
    print("Teleporting to Home.")
    teleport(home,2846,173)

def go_market():
    print("Teleporting to Market.")
    teleport(market,2130,804)