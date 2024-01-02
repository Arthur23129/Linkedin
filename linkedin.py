from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.common.exceptions import *
from time import sleep
import os
import random
import pyautogui

def iniciar_driver():

        chrome_options = Options()

        arguments = ['--lang=en-US', '--start-maximized']

        for argument in arguments:
            chrome_options.add_argument(argument)

        chrome_options.add_experimental_option('prefs', {
            'download.prompt_for_download': False,
            'profile.default_content_setting_values.notifications': 2,
            'profile.default_content_setting_values.automatic_downloads': 1

        })

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=chrome_options)
        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ]
        )
        return driver, wait

# area = pyautogui.prompt(text="digite a profissão da pessoa que você quer adicionar")
area = 'programador'
driver, wait = iniciar_driver()
from login import login
from login import password

nota = f'Meu nome é Arthur estudante de Python, sou aspirante a desenvolvedor. {os.linesep}Gostei bastante do seu perfil e adoraria lhe adicionar como contato. Abraço!'

driver.get('https://br.linkedin.com')
#logar no site
email = driver.find_element(By.XPATH, "//input[@id='session_key']")
email.send_keys(login)
senha = driver.find_element(By.XPATH, "//input[@id='session_password']")
senha.send_keys(password)
botao = driver.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn']")
botao.click()
#pesquisar pessoas
input('enter')
pesquisar = wait.until(condicao_esperada.visibility_of_element_located((By.XPATH, "//input[@placeholder='Pesquisar']")))
pesquisar.send_keys(area)
pesquisar.send_keys(Keys.ENTER)

filtros = wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH, "//li[@class='search-reusables__primary-filter']")))
filtros[2].click()


existe_proxima_pagina = True
while existe_proxima_pagina == True:
    sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollTop);")
    sleep(2)
    botoes_conectar = driver.find_elements(By.XPATH, "//button//span[text()='Conectar']")
    for botao_conectar in botoes_conectar:
            botao_conectar.click()
            sleep(random.randint(1,2))
            nome_sem_formatar = driver.find_element(By.XPATH, "//span[@class='flex-1']//strong")
            sleep(random.randint(1,2))
            nome = nome_sem_formatar.text
            sleep(random.randint(1,2))
            adicionar_nota = wait.until(condicao_esperada.visibility_of_element_located((By.XPATH, "//button[@aria-label='Adicionar nota']")))
            sleep(random.randint(1,2))
            adicionar_nota.click()

            mensagem = wait.until(condicao_esperada.visibility_of_element_located((By.XPATH, "//textarea[@name='message']")))
            sleep(random.randint(1,2))

            mensagem.send_keys (f'olá {nome}, {nota}')
            sleep(random.randint(1,2))

            enviar = driver.find_element(By.XPATH, "//button[@aria-label='Enviar agora']")
            sleep(random.randint(1,2))            
            enviar.click()
            sleep(random.randint(1,2))

    botoes_seguir = driver.find_elements(By.XPATH, "//button//span[text()='Seguir']")
    for botao_seguir in botoes_seguir:
        botao_seguir.click()
    try:
        proxima_pagina = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//button[@aria-label='Avançar']")))
        proxima_pagina.click()
        sleep(20)
    except:
        print('ultima pagina')
        existe_proxima_pagina == False
        driver.close()



input('acabou as pagina')