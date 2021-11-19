import keyboard  # input do teclado
import os
import time


def clearConsole(): return os.system('cls' if os.name in ('nt', 'dos')else 'clear')  # funcão para dar clear na consola


playerUp = True  # posiçao

print(">\n")  # posiçao inical

while True:
    try:
        if keyboard.is_pressed('up'):  # se clicar no up
            clearConsole()  # clear na consola
            if playerUp:
                print("\n>")  # troca de posiçao
                playerUp = False  # e troca o bool
                time.sleep(0.2)

            else:
                print(">\n")  # troca de posicao
                playerUp = True  # e troca o bool
                time.sleep(0.2)

    except:
        break
