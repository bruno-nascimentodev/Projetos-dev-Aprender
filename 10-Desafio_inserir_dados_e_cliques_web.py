# DESAFIO - Exercitar inserção de dados e clique em página web

# 1) Navegue até o site https://cursoautomacao.netlify.app/
# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
# 3) Clique em alerta, para gerar a alerta
# 4) Feche a alerta
# 5) Suba a página totalmente para cima
# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"


import webbrowser
import pyautogui as py
from time import sleep

py.PAUSE = 1.5

# Acessando a página
webbrowser.open('https://cursoautomacao.netlify.app/')

# Definindo funções para deixar código mais legível
def pesquisa(text):
    py.hotkey('Ctrl','f')
    py.write(text)
    py.hotkey('esc')
    py.hotkey('tab')

def ir_botao_clicar():
    py.hotkey('tab')
    py.hotkey('enter')

# Pesquisando a "Exemplo Alertas" e digitando meu nome
sleep(3)
pesquisa('alertas')
py.write('Bruno Moura do Nascimento')

# Clicar no alerta 
# Gerar o alerta 
ir_botao_clicar()

# Fechar o alerta
py.hotkey('enter')

# Subir a página por completo
py.hotkey('Ctrl','home')

# Seguir até a área de arquivos para downloads
pesquisa('planilha')

# Baixar arquivo EXCEL
ir_botao_clicar()
py.hotkey('esc') # Some com a notificação de downloads

# Baixar arquivo PDF
py.hotkey('tab')
ir_botao_clicar()

# Mensagem de Notificação
alerta = py.confirm(text='Você terminou com sucesso \n\nPressione OK para encerrar o bot',title='Parabéns !!!')
if alerta == 'OK':
    py.hotkey('Ctrl','w')