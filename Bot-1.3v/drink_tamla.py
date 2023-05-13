from staff import bottle,tamla_color,hunt_pack

from py_stealth import *

def tamla():
    if GetHP(Self()) < 250:
        if FindTypeEx(bottle,tamla_color,hunt_pack,False):
            UseObject(FindItem())