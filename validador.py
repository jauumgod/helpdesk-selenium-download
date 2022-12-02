from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

time.sleep(1)
def Validador_login():
    usuario = 'joao.marinho'
    senha = 'a1h2q4v1'
    global navegador
    navegador.get("https://helpdesk.grupokurujao.com.br/otrs/index.pl")
    time.sleep(2)
    #usuario
    navegador.find_element('xpath','//*[@id="User"]').click()
    navegador.find_element('xpath','//*[@id="User"]').send_keys(usuario)
    time.sleep(1)
    #password
    navegador.find_element('xpath','//*[@id="Password"]').click()
    navegador.find_element('xpath','//*[@id="Password"]').send_keys(senha)
    #login
    navegador.find_element('xpath','//*[@id="LoginButton"]').click()
    navegador.maximize_window()


def Abrir_chamado():
    #select type service
    navegador.find_element('xpath','//*[@id="nav-Tickets"]/a').click()
    navegador.find_element('xpath','//*[@id="nav-Tickets-Statusview"]/a').click()
    navegador.find_element('xpath','//*[@id="TicketID_160395"]/td[7]/div').click()
    time.sleep(2)

def create():
    nome = '01'
    imagem = navegador.save_screenshot('screenshot.png')
    open_pasta = os.path.join('//desktop//projects//selenium_save_screenshots')
    os.mkdir(open_pasta+nome)
    lista = os.listdir(open_pasta)
    print(lista)
    print('concluido')
    
    

Validador_login()
Abrir_chamado()
create()

time.sleep(1)
navegador.close()