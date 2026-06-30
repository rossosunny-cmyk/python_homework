from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Safari()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.NAME, "first-name"))
    ).send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

    zip_code_class = driver.find_element(By.ID, "zip-code").get_attribute(
        "class"
    )

    first_name_class = driver.find_element(By.ID, "first-name").get_attribute(
        "class"
    )
    last_name_class = driver.find_element(By.ID, "last-name").get_attribute(
        "class"
    )
    address_class = driver.find_element(By.ID, "address").get_attribute(
        "class"
    )
    email_class = driver.find_element(By.ID, "e-mail").get_attribute("class")
    phone_class = driver.find_element(By.ID, "phone").get_attribute("class")
    city_class = driver.find_element(By.ID, "city").get_attribute("class")
    country_class = driver.find_element(By.ID, "country").get_attribute(
        "class"
    )
    job_class = driver.find_element(By.ID, "job-position").get_attribute(
        "class"
    )
    company_class = driver.find_element(By.ID, "company").get_attribute(
        "class"
    )

    driver.quit()

    assert "danger" in zip_code_class
    assert "success" in first_name_class
    assert "success" in last_name_class
    assert "success" in address_class
    assert "success" in email_class
    assert "success" in phone_class
    assert "success" in city_class
    assert "success" in country_class
    assert "success" in job_class
    assert "success" in company_class
