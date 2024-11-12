# DESAFIO
# Crie um código com o pyautogui para que posicione o mouse em cima do monte de pedra;
# Clique em cima do monte de pedras, por meio de loop, para gerar pontuação 

import pyautogui as py
import time

# Movimentando atá a direção
py.moveTo(389,424, duration=0.5)

# Clique em cima do monte de pedra
for i in range(50):
    py.click()
    time.sleep(0.1)
    print(i)



