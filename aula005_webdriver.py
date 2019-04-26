from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class PesquisaGoogle:

    def __init__(self, driver):
        self.TEXTO_PESQUISA = (By.XPATH, "//input[@name='q']")
        self.SUBMIT_ESTOU_COM_SORTE = (
            By.XPATH, "//div[@class='FPdoLc VlcLAe']/center/input[@aria-label='Estou com sorte']")
        self.SUBMIT_LOGO = (By.XPATH, "//center/div/img[@id='hplogo']")
        self.SUBMIT_INICIAR = (By.XPATH, "//div[@class='start-button']/a[@href='#']")

        driver.get("http://www.google.com.br")
        driver.maximize_window()

    @staticmethod
    def scroll():
        element = driver.find_element(By.XPATH, "//a[@href='http://www.vivo.com.br'][text()='VIVO BHE']")
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.perform()

    def pesquisa_google(self, text):
        driver.find_element(*self.TEXTO_PESQUISA).send_keys(text)
        driver.find_element(*self.SUBMIT_LOGO).click()
        driver.find_element(*self.SUBMIT_ESTOU_COM_SORTE).click()
        driver.find_element(*self.SUBMIT_INICIAR).click()
        time.sleep(10)
        self.scroll()
        time.sleep(45)


driver = webdriver.Chrome()
test = PesquisaGoogle(driver)
test.pesquisa_google("teste")

driver.quit()
