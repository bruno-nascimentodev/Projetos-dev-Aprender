# DESAFIO - Curtir as 3 ultimas publicações do Canal DevAprender 
# por meio da localização de imagens

# PRÉ-REQUISITOS 
# Deixar a pagina do canal https://www.instagram.com/devaprender/ aberta em meia tela 
# Acessar a última publicação
# Criar uma pasta chamada img 
# Salvar a imagem de curtir dentro dela

import pyautogui as py
from time import sleep
import random

# Controla o número de repetoções de execução
for i in range(3):
    # Estabelce um tempo aleatório de execução
    tempo = random.randint(5,10)
    
    # Imprime tempo no terminal para acompanhmento
    print(tempo)

    # Localizando e curtindo publicação
    curtida = py.locateCenterOnScreen('./img/curtir.png')
    py.moveTo(curtida[0],curtida[1],duration=1)
    py.click()
    py.moveTo(700,674,duration=0.3)

    sleep(1)

    # Passando para próxima postagem
    py.press('right')

    # Tempo aleatório para não ser pego
    sleep(tempo)


# Informa ao usuário a conclusão da tarefa 
py.alert('Suas curtidas foram feitas com sucesso')