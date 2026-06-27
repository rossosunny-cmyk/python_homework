from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.get("http://the-internet.herokuapp.com/inputs")

try:
    input_field = browser.find_element(By.CSS_SELECTOR, "input[type='number']")
    input_field.send_keys("12345")
    input_field.clear()
    input_field.send_keys("54321")
finally:
    browser.quit()
