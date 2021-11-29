import keyboard
import os
import time

characters = 1


def clearConsole(): return os.system('cls' if os.name in ('nt', 'dos')
                                     else 'clear')


def characterSelection():
    global characters

    if keyboard.is_pressed('j'):
        if characters == 1:
            clearConsole()
            print("<< Human >>")
            characters += 1
            time.sleep(0.2)
        elif characters == 2:
            clearConsole()
            print("<< Teddy Bear >>")
            characters += 1
            time.sleep(0.2)
        elif characters == 3:
            clearConsole()
            print("<< Wizard >>")
            characters += 1
            time.sleep(0.2)
        elif characters == 4:
            clearConsole()
            print("<< Zack Freedman >>")
            characters += 1
            time.sleep(0.2)
        elif characters == 5:
            clearConsole()
            print("<< Shepherd >>")
            characters += 1
            time.sleep(0.2)

        else:
            characters = 1


while True:
    characterSelection() 
