from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

contatos = ['Saves', 'Testes']
mensagem = "Teste de envio"
midia = "..."
teste = "..."


def buscar_contato(contato):
    campo_pesquisa = driver.find_element(
        "xpath", '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element(
        "xpath", '//div[contains(@class,"fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv")]')
    campo_mensagem.click()
    time.sleep(3)
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)


def envia_midia(midia, teste):
    driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
    campo_midia = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    # time.sleep(2)
    campo_midia.send_keys(midia, teste)
    # campo_midia.send_keys(teste)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "span[data-icon='send']").click()


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
    envia_midia(midia, teste)
# copyable-text selectable-text
# fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv
