from py_stealth import *
from datetime import *
import timeit

chisel = 0x1026
tool = 0x1022
wood = 0x1BDD
bow = 0x68EC
box = 0x53DDDB89
leg = "Legendary"
exept = "Exceptional"
perf = "Perfect"
animal = "Animal"

def melt_bow():
    if FindType(bow, Backpack()) > 0:
        UseType(chisel, 0xFFFF)
        WaitTargetObject(FindType(bow, Backpack()))
        Wait(500)
        TargetToObject(Self())
        Wait(2500)

def check_legendary():
    while FindType(bow, Backpack()): 
        item_cliloc = GetCliloc(FindItem())
        if leg in item_cliloc:
            print("Наконец Легендарка!!! :)")
            MoveItem(FindItem(), 1, box, 0, 0, 0)
            print("Переложил в сундук.")
        elif perf in item_cliloc or exept in item_cliloc:
            print(f"Это {perf if perf in item_cliloc else exept}.")
            print("Переработать это говно!!!")
            melt_bow()
        else:
            print("Это вообще обычный лук! сразу на переработку!!!!")
            melt_bow()
    else:
        print("There is No Item To Check For")

def count_created_leg():
    UseObject(box)
    if FindTypeEx(bow, 0xFFFF, box, 0) and animal in GetCliloc(FindItem()):
        print(f"сделал {str(CountEx(bow, 0xFFFF, box))} лег луков.")
    else:
        print("сделал 0 лег луков.")
    
def craft_bow():
    CloseSimpleGump(-1)
    if FindType(tool, Backpack()):
        UseType2(tool)
        if FindType(wood, Backpack()):
            target_item = FindItem()
            WaitTargetObject(target_item)
            Wait(500)
            WaitGump(400)  # 120 skill
            Wait(500)
            WaitGump(55868)  # 120 skill
            start_time = datetime.now()
            WaitJournalLineSystem(start_time, "You stop.|Success.", 10000)
        else:
            print("There Is No Wood In Your Backpack.")
    else:
        print("There Is No Tool's Anymore.")
        Wait(1000)

def use_arms_lore():
    if FindType(bow, Backpack()) > 0:
        UseSkill('Arms Lore')
        WaitTargetObject(FindItem())
        Wait(500)
    else:
        print("There Is Nothing To Lore.")
        Wait(1000)

def check_wood_amount():
    if FindTypeEx(wood, 0xFFFF, Backpack(), 0):
        print(f"Осталось {FindFullQuantity()} дерево.")
    else:
        print("There is No Wood In Your Backpack.")

def main():
    craft_bow()
    use_arms_lore()
    check_legendary()
    ClearSystemJournal()
    check_wood_amount()
    count_created_leg()
    
if __name__ == '__main__':
    while True:
        main()

