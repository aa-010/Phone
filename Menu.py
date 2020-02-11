import sys
import os
import msvcrt
from termcolor import colored, cprint
import colorama
from colorama import Fore, Back, Style
colorama.init()

#menuItems = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]

def MainMenu(menuItems = 0, activeItem = 0):

    os.system('CLS')

    for i in range(len(menuItems)):
        if i != activeItem:
            print(menuItems[i])
        else:
            print(colored(menuItems[i], "green", "on_white"))
    print("Down - next item;    UP - previous item;   ESC - Exit;")

    if (activeItem == -1):
         return activeItem

    pressedKey = msvcrt.getch()
    
    if ord(pressedKey) == 13:
        return activeItem 
    activeItem = Select(activeItem, pressedKey, menuItems)        

    return MainMenu(menuItems, activeItem)

        
def Select(select = 0, pressedKey = 0, menuItems = 0):
    
    firstItem = 0
    lastItem = len(menuItems) - 1
        
    if ord(pressedKey) == 27:
        return -1

    elif ord(pressedKey) == 80:
        if select != lastItem:
            select += 1
        else: 
            select = firstItem

    elif ord(pressedKey) == 72:
        if select != firstItem:
            select -= 1
        else: 
            select = lastItem
        
    return select
   