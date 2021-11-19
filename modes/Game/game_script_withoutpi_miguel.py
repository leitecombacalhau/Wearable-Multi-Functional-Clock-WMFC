import os
import time
import keyboard

firstRowDisplay = '>'
secondRowDisplay = '\n'

playerShootFirstRowDisplay = ''
playerShootSecondRowDisplay = ''

playerMovementFirstRowDisplay = ''
playerMovementSecondRowDisplay = ''

bulletPos = 0
bulletChar = '⁜'
bulletSpaces = ''
playerUp = True


def clearConsole(): return os.system('cls' if os.name in ('nt', 'dos')
                                     else 'clear')


def playerShoot():
    global bulletChar
    global bulletPos
    global bulletSpaces

    global firstRowDisplay
    global secondRowDisplay

    while(bulletPos != 9):
        time.sleep(0.7)
        clearConsole()
        bulletPos += 1
        bulletSpaces = bulletSpaces+' '
        if firstRowDisplay == '\n':
            print(firstRowDisplay+secondRowDisplay+bulletSpaces+bulletChar)
        else:
            print(firstRowDisplay+bulletSpaces+bulletChar+secondRowDisplay)


def playerMovement():
    global playerUp
    global firstRowDisplay
    global secondRowDisplay

    clearConsole()
    if playerUp:
        playerUp = False
        firstRowDisplay = "\n"
        secondRowDisplay = ">"
        print(firstRowDisplay+secondRowDisplay)
        time.sleep(0.2)

    else:
        firstRowDisplay = ">"
        secondRowDisplay = "\n"
        print(firstRowDisplay+secondRowDisplay)
        playerUp = True
        time.sleep(0.2)


print(firstRowDisplay+secondRowDisplay)
while True:
    try:
        if keyboard.is_pressed('up'):
            playerMovement()
        elif keyboard.is_pressed('space'):
            playerShoot()
    except:
        break
