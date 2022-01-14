from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

contatos = open("./contatos.txt", 'r', encoding='UTF-8')
contatos = contatos.read()
contatos = contatos.split('\n')

print('\n--- ROBÔ WHATSAPP PARA ENVIO DE MENSAGENS ---')
print('Enviar texto [1]\nEnviar imagem [2]\nEnviar texto e imagem [3]')
opcao = input('\nDigite a sua opção: ')

class WhatsappBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        ser = Service("./chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def EnviarMensagens(self):
        mensagem = open("./mensagem.txt", 'r', encoding='UTF-8')
        mensagem = mensagem.read()
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        for contato in contatos:
            pesquisa = self.driver.find_element(By.CLASS_NAME, "_13NKt")
            time.sleep(2)
            pesquisa.click()
            time.sleep(2)
            pesquisa.send_keys(contato)
            time.sleep(2)
            pesquisa.send_keys(Keys.ENTER) 
            chat_box = self.driver.find_element(By.CLASS_NAME, 'p3_M1')
            time.sleep(3)
            chat_box.click()
            time.sleep(3)
            chat_box.send_keys(mensagem)
            botao_enviar = self.driver.find_element(By.XPATH,
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(10)
            
    def EnviarMidia(self):
        midia = "C:\\caminho\\para\\seu\\arquivo\\de\\midia.jpeg"
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        for contato in contatos:
            pesquisa = self.driver.find_element(By.CLASS_NAME, "_13NKt")
            time.sleep(2)
            pesquisa.click()
            time.sleep(2)
            pesquisa.send_keys(contato)
            time.sleep(2)
            pesquisa.send_keys(Keys.ENTER) 
            self.driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
            attach = self.driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            time.sleep(3)
            attach.send_keys(midia)
            time.sleep(5)
            botao_enviar = self.driver.find_element(By.XPATH,
                    "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(10)

    def EnviarAmbos(self):
        midia = "C:\\Users\\pluca\\OneDrive\\Documents\\Lucas\\Trabalho\\Python\\BotWhatsapp\\imagens\\mengo.jpg"
        mensagem = open("./mensagem.txt", 'r', encoding='UTF-8')
        mensagem = mensagem.read()
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        for contato in contatos:
            pesquisa = self.driver.find_element(By.CLASS_NAME, "_13NKt")
            time.sleep(2)
            pesquisa.click()
            time.sleep(2)
            pesquisa.send_keys(contato)
            time.sleep(2)
            pesquisa.send_keys(Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
            attach = self.driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            time.sleep(3)
            attach.send_keys(midia)
            time.sleep(5)
            botao_enviar = self.driver.find_element(By.XPATH,
                    "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)
            chat_box = self.driver.find_element(By.CLASS_NAME, 'p3_M1')
            time.sleep(3)
            chat_box.click()
            time.sleep(3)
            chat_box.send_keys(mensagem)
            botao_enviar = self.driver.find_element(By.XPATH,
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(10)

bot = WhatsappBot()

if opcao == "1":
    bot.EnviarMensagens()
if opcao == "2":
    bot.EnviarMidia()
if opcao == "3":
    bot.EnviarAmbos()