# DESAFIO - Rolar a página até um local específico
# Navegar na página do wikipedia Brasil e rolar a página até a seção de História

import pyautogui as py
from time import sleep

# Posiciona o mouse na tela 
py.moveTo(1417,235,duration=0.2)

# LOOP para rolar a página até chegar na Seção de História
for i in range(4):
    sleep(0.5)
    py.scroll(-950)

# Tempo para verificar o resultado
sleep(2)

# LOOP para retornar ao topo da página
for i in range(4):
    sleep(0.1)
    py.scroll(1000)
