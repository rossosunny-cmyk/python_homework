from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/classattr")

try:
    blue_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()

    WebDriverWait(browser, 5).until(ec.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()
finally:
    browser.quit()
