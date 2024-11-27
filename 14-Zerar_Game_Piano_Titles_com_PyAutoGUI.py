# Desafio - Zerar Game Piano Titles com PyAutoGUI

import pyautogui as py 
import keyboard
import win32api
import win32con
from time import sleep

py.click(1464,520,duration=1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('1') == False:
    if py.pixelMatchesColor(1271,421,(0,0,0)):
        click(1271,421)
    if py.pixelMatchesColor(1387,418,(0,0,0)):
        click(1387,418)
    if py.pixelMatchesColor(1477,418,(0,0,0)):
        click(1477,418)
    if py.pixelMatchesColor(1586,419,(0,0,0)):
        click(1586,419)



