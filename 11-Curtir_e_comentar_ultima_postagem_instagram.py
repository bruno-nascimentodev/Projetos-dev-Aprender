'''
# DESAFIO - Criar um script para curtir e comentar a última publicação de uma conta no instagram

1- Abrir navegador 
2- Acessar instagram 
3- Logar no instagram 
4- Ignorar salvamento de informações no navegador 
5- clicar em pesquisar conta de usuário 
6- Passar conta
7- Entrar na página
8- Clicar na postagem mais recente 
9- Verificar se já foi curtida a última postagem
10- Caso já tenha curtida não fazer nada, se não curtir foto
11- Comentar foto
12- Pausar bot por 24h
'''

import pyautogui as py 
import os
from time import sleep
import sys

py.PAUSE = 1

# Variáveis 
chrome = f'C:\Program Files\Google\Chrome\Application\chrome.exe'
url_instagram = f'https://www.instagram.com/'
login = 'xxxxxxxxxxxxxxx'
senha = 'xxxxxxxxxxx'
conta = 'adidasoriginals'
caminho_img = './img/insta/'

# Funções 
def status_script():
    print('\n\nLOG do Bot:')

def pressionar_vezes(tecla,vezes): # Define a quantidade de vezes que tecla será clicada
    for i in range(0,vezes):
        py.press(tecla,interval=0.5)

def pesquisar_palavra(palavra):# Pesquisa determinada palavra no navegador e da um tab
    py.hotkey('Ctrl','f')
    py.typewrite(palavra)
    py.hotkey('esc')
    py.hotkey('tab')

def pesquisar_clicar_palavra(palavra):# Pesquisa determinada palavra no navegador e clica em cima
    py.hotkey('Ctrl','f')
    py.typewrite(palavra)
    py.hotkey('esc')
    py.hotkey('enter')

def verifica_pag_carregada(img,nome_pagina):
    try:
        if py.locateOnScreen(f'{caminho_img}{img}',minSearchTime=15):
        #status_pag = True
            print(f"Página carregada - {nome_pagina}")
            #return status_pag
    except py.ImageNotFoundException:
            sys.exit(f'Encerrando o programa: Página não carregada. - {nome_pagina}')  

status_script()

# 1- Abrir navegador 
py.hotkey('Win','r')
py.typewrite(chrome) # Abri uma janela totalmente nova
py.press('enter')
verifica_pag_carregada('chrome.png','Chrome')
py.hotkey('Win','right') # Ajuste tela na lateral

# 2- Acessar instagram 
py.typewrite(url_instagram)
py.press('enter')

# 3- Logar no instagram 
verifica_pag_carregada('insta.png','Login Instagram')
pesquisar_palavra('telefone')
py.typewrite(login)
py.hotkey('tab')
py.typewrite(senha)
py.hotkey('enter')

# 4- Ignorar salvamento de informações no navegador 
#sleep(3)
verifica_pag_carregada('info_login.png','Info de Login')
pesquisar_clicar_palavra('Agora')

# 5- clicar em pesquisar conta de usuário 
#sleep(2)
verifica_pag_carregada('pag_principal_insta.png','Página Principal')
pesquisar = py.locateCenterOnScreen(f'{caminho_img}pesquisar.png')

py.moveTo(pesquisar[0],pesquisar[1],duration=0.5)
py.click()

# 6- Passar conta
py.typewrite(conta)

# 7- Entrar na página
sleep(1)
pressionar_vezes('tab',vezes=2)
py.hotkey('enter')

# 8- Clicar na postagem mais recente
verifica_pag_carregada('conta.png','Conta alvo')
pesquisar_palavra('marcados')
py.hotkey('enter')

# 9- Verificar se já foi curtida a última postagem
try:
    verifica_pag_carregada('postagem.png','Última postagem')
    curtir = py.locateCenterOnScreen('./img/insta/curtir.png')
    if curtir:
        print('STATUS - Curtir e comentar')
        py.moveTo(curtir[0], curtir[1], duration=0.5)
        py.click()
        # 10- Comentar foto
        pesquisar_clicar_palavra('adicione')
        py.typewrite('Oohu')
        py.hotkey('enter')
        sleep(2)
        py.hotkey('esc')
        menu = py.locateOnScreen('./img/insta/menu.png')
        if menu:
            py.moveTo(menu[0], menu[1], duration=0.5)
            py.click()
            pesquisar_clicar_palavra('sair')
            verifica_pag_carregada('saindo.png','Saindo')
            print('\n')
except py.ImageNotFoundException:
    #print("Imagem 'curtir.png' não encontrada, verificando 'curtida.png'.")
    print("STATUS - Curtida e comentário já realizados")

# 11- Caso já tenha curtida, verificar se a imagem 'curtida.png' está presente
    try: 
        curtida = py.locateOnScreen('./img/insta/curtida.png')
        if curtida:
            #print('Imagem curtida encontrada')
            sleep(2)
            py.hotkey('esc')
            menu = py.locateOnScreen('./img/insta/menu.png')
            if menu:
                py.moveTo(menu[0], menu[1], duration=0.5)
                py.click()
                pesquisar_clicar_palavra('sair')
                verifica_pag_carregada('saindo.png','Saindo')
                print('\n')
        else:
            print('Imagem "curtida.png" também não foi encontrada.')
    except py.ImageNotFoundException:
        print('Nenhuma das imagens foi encontrada. Nenhuma ação realizada.')
        
# 12- Pausar bot por 24h