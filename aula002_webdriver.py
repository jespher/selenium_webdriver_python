from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.google.com")

driver.set_page_load_timeout(10)

driver.find_element_by_id("hplogo")

# driver.find_element_by_class_name("")

# driver.find_element_by_css_selector("hplogo")

# driver.find_element_by_xpath("")

# driver.find_element_by_name("")

# driver.find_element_by_link_text("")

# driver.find_element_by_partial_link_text("")

print(driver.current_url)
print(driver.page_source)
print(driver.title)


driver.quit()
