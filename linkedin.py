import unittest
import time

from selenium import webdriver


class Linkedin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.linkedin.com/?originalSubdomain=br"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//form[@class='login-form']/input[@type='text']") \
            .send_keys("luis.88.rasini@gmail.com")
        time.sleep(4)
        driver.find_element_by_xpath("//form[@class='login-form']/input[2][@type='password']") \
            .send_keys("polosul21")
        time.sleep(4)
        driver.find_element_by_xpath("//form[@class='login-form']/input[3][@tabindex='1']") \
            .click()
        time.sleep(4)


def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()
