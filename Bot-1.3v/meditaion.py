from datetime import datetime
from py_stealth import *

def medit():
    if GetMana(Self()) < 250:
        if WarMode():
            SetWarMode(False)
        start_time = datetime.now()
        UseSkill("Meditation")
        Wait(500)
        if InJournalBetweenTimes("I am already performing another action.|You are already doing something else.",start_time,datetime.now()) != -1:
            Wait(5000)
        else:
            startime = datetime.now()
            WaitJournalLineSystem(startime,"You are already doing something else.|You stop meditating.|You moved and lost your concetration.",10000)
        