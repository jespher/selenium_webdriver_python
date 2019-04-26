from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com.br")
driver.maximize_window()

TEXTO_PESQUISA = (By.XPATH, "//input[@name='q']")
SUBMIT_ESTOU_COM_SORTE = (By.XPATH, "//div[@class='FPdoLc VlcLAe']/center/input[@aria-label='Estou com sorte']")
SUBMIT_LOGO = (By.XPATH, "//center/div/img[@id='hplogo']")
SUBMIT_INICIAR = (By.XPATH, "//div[@class='start-button']/a[@href='#']")


def scroll():
    element = driver.find_element(By.XPATH, "//a[@href='http://www.vivo.com.br'][text()='VIVO BHE']")
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()


def pesquisa_google(text):
    driver.find_element(*TEXTO_PESQUISA).send_keys(text)
    driver.find_element(*SUBMIT_LOGO).click()
    driver.find_element(*SUBMIT_ESTOU_COM_SORTE).click()
    driver.find_element(*SUBMIT_INICIAR).click()
    time.sleep(10)
    scroll()
    time.sleep(45)


pesquisa_google("teste")

driver.quit()
