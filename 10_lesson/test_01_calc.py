import allure
from selenium import webdriver

from calculator_page import CalculatorPage


@allure.title("Проверка медленного калькулятора")
@allure.description("Проверка сложения 7 + 8 с задержкой результата.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    with allure.step("Открыть браузер Chrome"):
        driver = webdriver.Chrome()

    with allure.step("Открыть страницу калькулятора"):
        calculator_page = CalculatorPage(driver)
        calculator_page.open()

    with allure.step("Установить задержку 45 секунд"):
        calculator_page.set_delay("45")

    with allure.step("Нажать кнопки 7, +, 8, ="):
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

    with allure.step("Получить результат"):
        result = calculator_page.get_result("15")

    with allure.step("Закрыть браузер"):
        driver.quit()

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15"
