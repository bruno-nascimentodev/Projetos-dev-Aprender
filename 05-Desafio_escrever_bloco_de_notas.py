# DESAFIO - Escrever texto com caracteres especiais 
# Crie um programa que vai até onde seu bloco de notas estiver aberto e digita a frase 
# Automação é Incrível

import pyautogui as py
import pyperclip
from time import sleep

py.click(1400,423,duration=0.5)

sleep(1)

def escrever_frase(frase):
    pyperclip.copy(frase)
    py.hotkey('Ctrl','v')

escrever_frase('Automação é Incrível!')


