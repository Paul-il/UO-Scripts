from recalls import home,charge_runebook,market,hunt_event
from load_unload_staff import unload,load
from change_class import crafter,hunter
from repair_items import repair_kryss,repair_bow
from datetime import datetime
from py_stealth import *

def main():
    start_main = datetime.now()
    SetMoveOpenDoor(True)
    SetMoveCheckStamina(True)
    for i in range(8):
        started = datetime.now()
        print(f"{i+1}-й круг охоты")
        with open("location/file_cast.txt", 'w+') as f:
            f.readlines()
        hunt_event()
        home()
        unload()
        load()
        charge_runebook()
        charge_runebook()
        ClearSystemJournal()
        print(f"{i+1}-й круг охоты")
        ended = datetime.now()
        res_time = ended - started
        print(res_time)
        print("Начал отдых после охоты.")
        
    with open("location/file_cast.txt", 'w+') as f:
        f.readlines()        
    hunt_event()
    market()
    crafter()
    home()
    repair_kryss()
    repair_bow()
    market()
    hunter()
    home()
    unload()
    load()
    charge_runebook()
    charge_runebook()
    ClearSystemJournal()
    end_start = datetime.now()
    res_main = end_start - start_main
    print(f"закончил за: {res_main}")
    print("Начал отдых после охоты.")
 


if __name__ == "__main__":
    while True:
        main()