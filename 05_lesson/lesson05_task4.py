from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.get("http://the-internet.herokuapp.com/login")

try:
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    login_button = browser.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']",
    )

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    login_button.click()

    success_message = browser.find_element(By.ID, "flash")
    print(success_message.text)
finally:
    browser.quit()