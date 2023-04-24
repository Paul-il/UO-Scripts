from py_stealth import *
from datetime import *
import timeit

def cart():
    UseSkill("Cartography")
    WaitMenu('What', 'Local Map')
    #WaitMenu('What', 'Regional Map') # 55 skill
    Wait(11000)

def main():
	cart()
    

if __name__ == '__main__':
    while (True):
        main()