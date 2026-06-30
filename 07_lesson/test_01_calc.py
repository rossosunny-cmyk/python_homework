from selenium import webdriver

from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()

    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.set_delay("45")
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    result = calculator_page.get_result("15")

    driver.quit()

    assert result == "15"
