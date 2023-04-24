from py_stealth import *
from datetime import *
import timeit


def hiding():
    if Hidden():
        UseSkill("Stealth")
        Wait(10000)
    else: 
        UseSkill("Hiding")
        Wait(10000)
        UseSkill("Stealth")
        Wait(10000)

if __name__ == "__main__":
    while True:
        hiding()