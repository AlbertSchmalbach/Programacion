from selenium import webdriver
from selenium.webdriver.common.by import By

# options = webdriver.EdgeOptions()
# options.add_experimental_option("detach", True)
# browser = webdriver.Edge(options=options)
# browser.implicitly_wait(10)
# browser.get("https://www.jw.org/es/")
# link = browser.find_element(By.CSS_SELECTOR, ".tertiaryButton")
# link.click()

# input_lenguaje = browser.find_element(By.CSS_SELECTOR, "li[lang=en]")
# input_lenguaje.click()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Edge(options=options)
browser.implicitly_wait(10)
browser.get("https://www.google.com.co")
link = browser.find_element(By.CSS_SELECTOR, ".gb_E")
link.click()

email_input = browser.find_element(By.ID, "identifierId")

email_input.send_keys("beto21048@gmail.com")


