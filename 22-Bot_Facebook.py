# Projeto 2 - Bot de Postagem no facebook

# Importação de Bibliotecas
from selenium import webdriver
# Importando argumentos necessários para a execução correta do selenium 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import random

# Configuração de drive
def iniciar_drive():

    chrome_options = Options()

    # Fonte de opções de switches - opções que podem ser usadas no navegador 
    # https://peter.sh/experiments/chromium-command-line-switches/


    arguments = [
        '--lan=pt-BR', # Definindo idioma da página
        '--window-size=800,800', # Definindo tamanho da janela 
        #'--headless',
        #'--start-maximized',
        '--incognito' # Definindo modo anonimo da janela
        
    ]

    ''' Para ser usada no vetor de argumentos
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''

    for argument in arguments:
        chrome_options.add_argument(argument)

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir realizar multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver

    # Obtém as dimensões da tela do sistema
    screen_width = driver.execute_script("return screen.width")
    screen_height = driver.execute_script("return screen.height")

    # Define a posição da janela para começar na metade esquerda da tela
    # E define o tamanho da janela (metade da largura da tela)
    driver.set_window_position(0, 0)  # Move a janela para a esquerda
    driver.set_window_size(screen_width // 2, screen_height)  # Tamanho da janela para metade da tela

def digitar_texto(texto,elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,5)/30)


driver = iniciar_drive()

# DECLARAÇÃO DE VARIÁVEIS 
email_text = 'xxxxxxxxx@xxxx.xxxx'
senha_text = 'xxxxxxxxx'

# NAVEGARA ATÉ A PÁGINA 
driver.get('https://www.facebook.com/')
sleep(1)

# BUSCAR E PASSAR LOGIN
email = driver.find_element(By.ID,'email')
digitar_texto(email_text,email)
sleep(1)

# BUSCAR E PASSAR SENHA
senha = driver.find_element(By.ID,'pass')
digitar_texto(senha_text,senha)
sleep(1)

# CLICAR ENTRAR
botao_entrar = driver.find_element(By.XPATH, "//button[@type='submit']")
botao_entrar.click()
sleep(10)

# CLICAR NA LOGO FACEBOOK
logo_face = driver.find_element(By.XPATH, "//*[@class='xe3v8dz' and @d='M13.651 35.471v-11.97H9.936V18h3.715v-2.37c0-6.127 2.772-8.964 8.784-8.964 1.138 0 3.103.223 3.91.446v4.983c-.425-.043-1.167-.065-2.081-.065-2.952 0-4.09 1.116-4.09 4.025V18h5.883l-1.008 5.5h-4.867v12.37a18.183 18.183 0 0 1-6.53-.399Z']")
logo_face.click()
sleep(5)

# BUSCAR CAMPO NO QUE ESTOU PENSANDO 
botao_msg = driver.find_element(By.XPATH,"//span[text()='No que você está pensando, Automa?']")
botao_msg.click()
sleep(5)


# ESCREVER UMA MENSAGEM
campo_msg = driver.find_element(By.XPATH,"//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
sleep(1)
campo_msg.click()
sleep(1)
campo_msg.send_keys("Olá! Bom dia a todos")
sleep(1)

# CLICAR EM PUBLICAR 
botao_publicar = driver.find_element(By.XPATH,"//div[@class='x1ja2u2z x78zum5 x2lah0s x1n2onr6 xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")
botao_publicar.click()



input('')