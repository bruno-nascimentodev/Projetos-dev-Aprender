# Desafio 03 - Marque o checkbox "Conversível" e "Off-Road"

# Importação de Bibliotecas
from selenium import webdriver
# Importando argumentos necessários para a execução correta do selenium 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Configuração de drive
def iniciar_drive():

    chrome_options = Options()

    # Fonte de opções de switches - opções que podem ser usadas no navegador 
    # https://peter.sh/experiments/chromium-command-line-switches/


    arguments = [
        '--lan=pt-BR', # Definindo idioma da página
        '--window-size=800,600', # Definindo tamanho da janela 
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

driver = iniciar_drive()

def busca_elemento(caminho):
    elemento = driver.find_element(By.XPATH,caminho)
    return elemento

# Entrando na página
# driver.get('https://cursoautomacao.netlify.app/')
driver.get('https://cursoautomacao.netlify.app/desafios')

# Rolando a página até o elemento
driver.execute_script('window.scrollTo(0, 800)')

sleep(1)

# Buscando os elementos
botao_conversivel = driver.find_element(By.XPATH,"//input[@id='conversivelcheckbox']")
botao_off = driver.find_element(By.XPATH,"//input[@id='offroadcheckbox']")

# Clicando nos elementos
sleep(1)
botao_conversivel.click()
botao_off.click()


input('')