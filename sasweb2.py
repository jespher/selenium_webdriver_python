import unittest
import time

from selenium import webdriver


class Sasweb_2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.1.110.10/homologacao/#/login"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//html/body/md-content/div/div/div[2]/form/div/input[@type='text']") \
            .send_keys("arquitetura")
        time.sleep(4)
        driver.find_element_by_xpath("//html/body/md-content/div/div/div[2]/form/div/input[@type='password']") \
            .send_keys("@RQUI1234")
        time.sleep(4)
        driver.find_element_by_xpath("//div/button[@class='md-raised md-primary md-button md-ink-ripple']") \
            .click()
        time.sleep(40)


def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()
