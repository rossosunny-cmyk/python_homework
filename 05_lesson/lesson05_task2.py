from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/dynamicid")

try:
    blue_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()
finally:
    browser.quit()
