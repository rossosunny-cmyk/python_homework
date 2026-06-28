from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL = "https://the-internet.herokuapp.com/dynamic_loading/2"
SCREENSHOT_PATH = Path(__file__).parent / "dynamic_loading.png"


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get(URL)

    wait = WebDriverWait(driver, 20)
    start_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    start_button.click()

    result_text = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    driver.save_screenshot(str(SCREENSHOT_PATH))
    actual_text = result_text.text
    driver.quit()

    assert actual_text == "Hello World!"
