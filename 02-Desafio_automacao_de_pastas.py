# DESAFIO - Automação de Pastas
# Entre em alguma pasta no seu PC e criar uma nova pasta usando Pyautogui

# REQUISITOS
# Windows Explorer deve estar aberto do lado esquerdo em meia tela na horizontal

import pyautogui as py
import time

# Movimento do mouse até a região do windows explorer
py.moveTo(758,408,duration=0.5)

# Clica com o botão direito na região
py.rightClick()

# Posiciona o mouse em ciam da opção Novo
py.move(100,200,duration=0.5)

# Clica na opção Novo
py.click()

# Posiciona o mouse em cima da opção Pasta
py.move(400,0,duration=0.5)

# Clica na opção Pasta
py.click()

# Aguarda até a pasta ser criada
time.sleep(0.5)

# Nomeia a pasta 
py.typewrite('Dev Aprender')

# Conclui a criação
py.hotkey('enter')