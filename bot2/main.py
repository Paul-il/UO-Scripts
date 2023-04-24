from recalls import teleport,charge_runebook,hunt
from load_unload_staff import unload,load
from change_class import crafter,hunter
from repair_items import repair_kryss,repair_bow

import time
from datetime import datetime
from py_stealth import *

def main():
    start_main = datetime.now()
    SetMoveOpenDoor(True)
    SetMoveCheckStamina(True)
    for i in range(8):
        started = datetime.now()
        print(f"{i+1}-й круг охоты")
        print(str(GetStr(Self())))
        hunt()
        teleport(1031,2846,173)
        unload()
        load()
        charge_runebook()
        ClearSystemJournal()
        print(f"{i+1}-й круг охоты")
        ended = datetime.now()
        res_time = ended - started
        print(res_time)
        print("Начал отдых после охоты.")
        for i in range(10):
            time.sleep(60)
            print(f"прошла {i+1}-я минут отдыха после охоты.")
        
    with open("location/file_cast.txt", 'w+') as f:
        f.readlines()        
    hunt()
    teleport(1025,2130,804)
    crafter()
    teleport(1031,2846,173)
    repair_kryss()
    repair_bow()
    teleport(1025,2130,804)
    hunter()
    teleport(1031,2846,173)
    unload()
    load()
    charge_runebook()
    ClearSystemJournal()
    end_start = datetime.now()
    res_main = end_start - start_main
    print(f"закончил за: {res_main}")
    print("Начал отдых после охоты.")
    for i in range(10):
        time.sleep(60)
        print(f"прошла {i+1}-я минут отдыха после охоты.")


if __name__ == "__main__":
    timea = datetime.now()
    while True:
        main()
        if timea.hour > 16:
            time.sleep(7*60)
        else:
            continue
