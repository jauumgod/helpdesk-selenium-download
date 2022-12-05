from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

os.system('cls')
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
    navegador.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    imagem = navegador.save_screenshot('./imagens/screenshot.png')
    lista = os.listdir('./imagens')
    print(lista)
    print('concluido')

def web_scraping():
    dados = navegador.find_element('xpath','/html/body/text()[2]').text()
    print(dados)
    

Validador_login()
Abrir_chamado()
create()
web_scraping()

time.sleep(1)
navegador.close()