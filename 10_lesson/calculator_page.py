from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Page Object для страницы медленного калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Создать объект страницы.

        Args:
            driver: экземпляр WebDriver.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """
        Открыть страницу калькулятора.

        Returns:
            None.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, value: str) -> None:
        """
        Ввести значение задержки в поле Delay.

        Args:
            value: значение задержки в секундах.

        Returns:
            None.
        """
        delay_input = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, button_text: str) -> None:
        """
        Нажать кнопку калькулятора по тексту.

        Args:
            button_text: текст кнопки калькулятора.

        Returns:
            None.
        """
        self.driver.find_element(
            By.XPATH,
            f"//span[text()='{button_text}']",
        ).click()

    def get_result(self, expected_result: str) -> str:
        """
        Дождаться результата и вернуть текст с экрана калькулятора.

        Args:
            expected_result: ожидаемый текст результата.

        Returns:
            Текст результата на экране калькулятора.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"),
                expected_result,
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
