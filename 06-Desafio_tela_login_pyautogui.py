# DESAFIO - Criar uma tela de login e senha salvando os dados passados em um bloco de notas

import pyautogui as py
import os
from time import sleep
import pyperclip 

py.PAUSE = 0.5

# Solicitar login usuário
login = py.prompt(title='Tela de Login', text='Digite seu email:')

# Solicitar senha usuário
senha = py.password(title='Tela de Login', text='Digite sua senha:', mask='*')

# Abrir bloco de nota  
os.system('notepad.exe')

# Passar dados coletados  
def passar_dados(text):
    pyperclip.copy(text)
    py.hotkey('Ctrl','c')

def colar_dados():
    py.hotkey('Ctrl','v')


sleep(1)
passar_dados(f'Login: {login}\nSenha: {senha}')
colar_dados()




