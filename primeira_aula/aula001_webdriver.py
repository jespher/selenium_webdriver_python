from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.google.com")

# element = driver.find_element_by_xpath("//input[@name='btnI']")  # Funciona

element = driver.find_element_by_css_selector("input[name='btnK']")  # Funciona

# element2 = driver.find_element_by_css_selector("input[name='btnI']")  # Funciona

# element = driver.find_element_by_css_selector("input[value='Estou com sorte']") # Funciona


value_button = element.get_attribute('value')
# print(value_button)
# print(element2.get_attribute('value'))

assert "Pesquisa Google" == value_button

driver.quit()
