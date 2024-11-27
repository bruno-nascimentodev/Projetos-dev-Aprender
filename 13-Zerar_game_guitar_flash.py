# Desafio - Zerar o jogo do guitar flash com o maior número de acertos

import pyautogui as py
from time import sleep
import keyboard

# Modo de saída do loop 
# Enquanto não for pressionado 1, não saíra do loop 
while keyboard.is_pressed('1') == False:
    # Verfifica a presença de uma cor em uma determinada região 
    # Botão Verde
    if py.pixelMatchesColor(1246,755,(0,152,0)):
        py.press('a')
        sleep(0.04)

    # Botão Vermelho
    if py.pixelMatchesColor(1333,751,(255,0,0)):
        py.press('s')
        sleep(0.04)

    # Botão Amarelo
    if py.pixelMatchesColor(1431,754,(244,244,2)):
        py.press('j')
        sleep(0.04)
