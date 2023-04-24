from py_stealth import *
from datetime import *

animal = 0x00125988

def cast():
    start = datetime.now()
    Wait(2000)
    #UOSay("all i need to say is a, otherwise i will be disconnected!")
    if InJournalBetweenTimes('cast me', start, datetime.now()) != -1:
        #AddToSystemJournal('Matching words')
        CastToObj("dispel",animal)
        Wait(1700)
        CastToObj("cunning",animal)
        Wait(1100)
        CastToObj("agility",animal)
        Wait(1100)
        CastToObj("bless",animal)
        Wait(1200)
        CastToObj("arch protection",animal)
        Wait(1700)
        CastToObj("strength",animal)
        Wait(1000)
        UseSkill("Meditation")
    else:
       pass
       
if __name__ == "__main__":
    while True:
        cast()