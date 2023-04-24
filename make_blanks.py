from py_stealth import *
from datetime import *
import timeit

scroll_blank = 0x0E34
tinkering_tools = 0x1EBA
logs = 0x1BDD
#3636   scroll_blank

def organaise():
    if FindType(scroll_blank, Backpack()):
        MoveItem(FindItem(),-1,Backpack(),0,0,0)
        ClearSystemJournal()
        print(f'изготовлено {CountEx(scroll_blank,0xFFFF,Backpack())} бланков, и осталось {CountEx(logs,0xFFFF,Backpack())} логов.')
        print(f'Осталось {CountEx(tinkering_tools,0xFFFF,Backpack())} Тинкер тулов. ')


def make_blanks():
    if FindType(logs, Backpack()):
        CloseSimpleGump(-1)
        UseType2(tinkering_tools)
        WaitTargetObject(FindItem())
        Wait(500)
        WaitGump(200)
        Wait(500)
        WaitGump(3636)
        startime = datetime.now()
        WaitJournalLineSystem(startime,"You stop.|Success.",10000)
        Wait(800)

if __name__ == '__main__':
    while True:
        make_blanks()
        organaise()