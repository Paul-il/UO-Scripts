from py_stealth import *
from datetime import *
import timeit

trash = 0x51BB18E4
drop_carp = 0x0ACD
x = 2145                      # Это х тайл
y = 839
color = 0x0000
sumka = 0x53A6334A

def drop_kovri():
    if FindTypeEx(drop_carp,color,sumka,0) > 0:
        MoveItem(FindItem(),0,trash,x,y,0)
        Wait(900)
    #AddToSystemJournal('Выбросил ковер')

def main():
	drop_kovri()
    

if __name__ == '__main__':
    while (True):
        main()